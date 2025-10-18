from sqlalchemy.orm import Session
from app.models.userdata import UserData
# from app.core.security import get_password_hash


class UserDataService:
    def __init__(self, db: Session):
        self.db = db

    def get_userdata(self, user_id: int):
        return self.db.query(UserData).filter(UserData.UserID == user_id).all()

    def get_userdata_id(self, user_id: int, user_data_id: int):
        return self.db.query(UserData).filter(UserData.UserID == user_id).filter(UserData.UserDataID == user_data_id).first()
