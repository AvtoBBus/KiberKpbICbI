from sqlalchemy.orm import Session
from app.models.meal import Meal
# from app.core.security import get_password_hash

class MealService:
    def __init__(self, db: Session):
        self.db = db
       
    '''
    Получение приема пищи по meal_id
    '''
    def get_meal_id(self, user_id: int, meal_id: int):
        return self.db.query(Meal).filter(Meal.UserID == user_id).filter(Meal.MealID == meal_id).first()
    
    '''
    Получение всех приемов пищи пользователя
    '''
    def get_meal(self, user_id: int):
        return self.db.query(Meal).filter(Meal.UserID == user_id).all()