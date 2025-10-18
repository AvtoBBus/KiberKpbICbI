from sqlalchemy.orm import Session
from app.models.statisticwh import StatisticWh
# from app.core.security import get_password_hash

class StatisticWhService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_statisticwh_id(self, user_id: int, statisticwh_id: int):
        return self.db.query(StatisticWh).filter(StatisticWh.UserID == user_id).filter(StatisticWh.StatisticWHID == statisticwh_id).first()
    
    def get_statisticwh(self, user_id: int):
        return self.db.query(StatisticWh).filter(StatisticWh.UserID == user_id).all()