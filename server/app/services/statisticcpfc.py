from sqlalchemy.orm import Session
from app.models.statisticcpfc import StatisticCPFC
# from app.core.security import get_password_hash

class StatisticCPFCService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_statisticwh_id(self, user_id: int, statisticcpfc_id: int):
        return self.db.query(StatisticCPFC).filter(StatisticCPFC.UserID == user_id).filter(StatisticCPFC.StatisticCPFCID == statisticcpfc_id).first()
    
    def get_statisticwh(self, user_id: int):
        return self.db.query(StatisticCPFC).filter(StatisticCPFC.UserID == user_id).all()