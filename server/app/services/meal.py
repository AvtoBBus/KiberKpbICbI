from sqlalchemy.orm import Session
from app.models.meal import Meal
from app.models.foodinmeal import FoodInMeal
from app.schemas.meal import MeaDTOPost
# from app.core.security import get_password_hash

class MealService:
    def __init__(self, db: Session):
        self.db = db
       
    def get_meal_id(self, user_id: int, meal_id: int):
        return self.db.query(Meal).filter(Meal.UserID == user_id).filter(Meal.MealID == meal_id).first()
    
    def get_meal(self, user_id: int):
        return self.db.query(Meal).filter(Meal.UserID == user_id).all()
    
    def add_meal(self, user_id: int, new_meal: MeaDTOPost):
        
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