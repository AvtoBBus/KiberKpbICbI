from sqlalchemy.orm import Session
from app.models.user import User
# from app.core.security import get_password_hash


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.UserID == user_id).first()