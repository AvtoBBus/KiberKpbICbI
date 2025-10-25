from sqlalchemy.orm import Session
from app.models.meal import Meal
from app.models.foodinmeal import FoodInMeal
from app.models.food import Food
from app.schemas.meal import MealDTOPut, MealDTOPost
from typing import List, Any
from sqlalchemy.orm import joinedload


class MealService:
    def __init__(self, db: Session):
        self.db = db

    def get_meal_id(self, user_id: int, meal_id: int):
        return self.db.query(Meal).filter(Meal.UserID == user_id).options(
            joinedload(Meal.FoodInMeals).joinedload(FoodInMeal.Food)
        ).filter(Meal.MealID == meal_id).first()

    def get_meal(self, user_id: int) -> List[Any]:
        return self.db.query(Meal).filter(Meal.UserID == user_id).options(
            joinedload(Meal.FoodInMeals).joinedload(FoodInMeal.Food)
        ).all()

    def add_meal(self, user_id: int, new_meal: MealDTOPost):

        findedFood = self.db.query(Food).filter(
            Food.FoodID == new_meal.FoodID
        ).first()

        if not findedFood:
            raise ValueError

        insertedMeal = Meal(
            Date=new_meal.Date,
            MealType=new_meal.MealType,
            UserID=user_id
        )

        self.db.add(insertedMeal)
        self.db.commit()


        insertedFoodInMeal = FoodInMeal(
            MealID=insertedMeal.MealID,
            FoodID=new_meal.FoodID,
            Weight=new_meal.Weight
        )

        self.db.add(insertedFoodInMeal)
        self.db.commit()

        return insertedMeal

    def edit_meal(self, user_id: int, new_meal: MealDTOPut):
        findedForUser = self.db.query(Meal).filter(Meal.UserID == user_id)

        findedMeal = findedForUser.filter(
            Meal.MealID == new_meal.MealID).first()

        if not findedMeal:
            raise ValueError

        findedMeal.MealType = new_meal.MealType
        findedMeal.Date = new_meal.Date

        findedFIMs = self.db.query(FoodInMeal).filter(FoodInMeal.MealID == new_meal.MealID).all()

        if len(findedFIMs) > len(new_meal.Products):
            count = 0
            for i in range(len(new_meal.Products)):
                findedFood = self.db.query(Food).filter(Food.FoodID == new_meal.Products[i].FoodID).first()

                if not findedFood:
                    raise ValueError

                findedFIMs[i].FoodID = new_meal.Products[i].FoodID
                findedFIMs[i].Weight = new_meal.Products[i].Weight
                count += 1

            for i in range(len(findedFIMs) - 1, count - 1, -1):
                self.db.delete(findedFIMs[i])

        else:
            count = 0
            for i in range(len(findedFIMs)):
                
                findedFood = self.db.query(Food).filter(Food.FoodID == new_meal.Products[i].FoodID).first()

                if not findedFood:
                    raise ValueError

                findedFIMs[i].FoodID = new_meal.Products[i].FoodID
                findedFIMs[i].Weight = new_meal.Products[i].Weight
                count += 1
            
            if count < len(new_meal.Products):
                for i in range(count, len(new_meal.Products)):

                    findedFood = self.db.query(Food).filter(Food.FoodID == new_meal.Products[i].FoodID).first()

                    if not findedFood:
                        raise ValueError

                    insertedFoodInMeal = FoodInMeal(
                        MealID=new_meal.MealID,
                        FoodID=new_meal.Products[i].FoodID,
                        Weight=new_meal.Products[i].Weight
                    )
                    self.db.add(insertedFoodInMeal)

        self.db.commit()

        return findedMeal

    def delete_meal(self, user_id: int, meal_id: int):
        findedForUser = self.db.query(Meal).filter(Meal.UserID == user_id)

        findedMeal = findedForUser.filter(Meal.MealID == meal_id).first()
        findedFoodInMeal = self.db.query(FoodInMeal).filter(
            FoodInMeal.MealID == meal_id).all()

        if (not findedMeal) or (len(findedFoodInMeal) == 0):
            raise ValueError

        self.db.delete(findedMeal)
        for fim in findedFoodInMeal:
            self.db.delete(fim)

        self.db.commit()

        return None
