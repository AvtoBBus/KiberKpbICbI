from sqlalchemy.orm import Session
from app.models.statisticcpfc import StatisticCPFC
from app.schemas.statisticcpfc import StatisticCPFCDTO
# from app.core.security import get_password_hash

class StatisticCPFCService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_statisticwh_id(self, user_id: int, statisticcpfc_id: int):
        return self.db.query(StatisticCPFC).filter(StatisticCPFC.UserID == user_id).filter(StatisticCPFC.StatisticCPFCID == statisticcpfc_id).first()
    
    def get_statisticwh(self, user_id: int):
        return self.db.query(StatisticCPFC).filter(StatisticCPFC.UserID == user_id).all()
        
    def add_statisticcpfc(self, user_id: int, new_statisticcpfc: StatisticCPFCDTO):

        inserted = StatisticCPFC(
            Date = new_statisticcpfc.Date,
            Calories = new_statisticcpfc.Calories,
            Protein = new_statisticcpfc.Protein,
            Fat = new_statisticcpfc.Fat,
            Carbonates = new_statisticcpfc.Carbonates,
            UserID = user_id
        )

        self.db.add(inserted)
        self.db.commit()

        return inserted
    
    def edit_statisticcpfc(self, user_id: int, new_statisticcpfc: StatisticCPFCDTO):

        findedForUser = self.db.query(StatisticCPFC).filter(StatisticCPFC.UserID == user_id)

        findedStat = findedForUser.filter(StatisticCPFC.StatisticCPFCID == new_statisticcpfc.StatisticCPFCID).first()

        if not findedStat:
            raise ValueError

        findedStat.Date = new_statisticcpfc.Date
        findedStat.Calories = new_statisticcpfc.Calories
        findedStat.Protein = new_statisticcpfc.Protein
        findedStat.Fat = new_statisticcpfc.Fat
        findedStat.Carbonates = new_statisticcpfc.Carbonates

        self.db.commit()

        return findedStat