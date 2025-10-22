from sqlalchemy.orm import Session
from app.models.food import Food
from app.schemas.food import FoodDTOPost
# from app.core.security import get_password_hash

class FoodService:
    def __init__(self, db: Session):
        self.db = db
       
    def get_food_id(self, food_id: int):
        return self.db.query(Food).filter(Food.FoodID == food_id).first()
    
    def get_food(self):
        return self.db.query(Food).all()

    def add_food(self, new_food: FoodDTOPost):

        inserted = Food(
            Name=new_food.Name,
            CategoryID=new_food.CategoryID,
            Calories=new_food.Calories,
            Protein=new_food.Protein,
            Fats=new_food.Fats,
            Carbonates=new_food.Carbonates
        )

        self.db.add(inserted)
        self.db.commit()

        return inserted