from sqlalchemy.orm import Session
from app.models.food import Food
# from app.core.security import get_password_hash

class FoodService:
    def __init__(self, db: Session):
        self.db = db
       
    def get_food(self, food_id: int):
        return self.db.query(Food).filter(Food.FoodID == food_id).first()
    
    def get_foods(self):
        return self.db.query(Food).all()