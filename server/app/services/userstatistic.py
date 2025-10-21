from sqlalchemy.orm import Session
from app.models.userstatistic import UserStatistic
# from app.core.security import get_password_hash

class UserStatisticService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_userstatistic(self, user_id: int):
        return self.db.query(UserStatistic).filter(UserStatistic.UserID == user_id).all()