from sqlalchemy.orm import Session
from app.models.statisticwh import StatisticWH
from app.schemas.statisticwh import StatisticWHDTO
# from app.core.security import get_password_hash

class StatisticWHService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_statisticwh_id(self, user_id: int, statisticwh_id: int):
        return self.db.query(StatisticWH).filter(StatisticWH.UserID == user_id).filter(StatisticWH.StatisticWHID == statisticwh_id).first()
    
    def get_statisticwh(self, user_id: int):
        return self.db.query(StatisticWH).filter(StatisticWH.UserID == user_id).all()
    
    def add_statisticwh(self, user_id: int, new_statisticwh: StatisticWHDTO):

        inserted = StatisticWH(
            Date = new_statisticwh.Date,
            Height = new_statisticwh.Height,
            Weight = new_statisticwh.Weight,
            UserID = user_id
        )

        self.db.add(inserted)
        self.db.commit()

        return inserted