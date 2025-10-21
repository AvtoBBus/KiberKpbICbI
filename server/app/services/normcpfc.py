from sqlalchemy.orm import Session
from app.models.normcpfc import NormCPFC
from app.schemas.normcpfc import NormCPFCRequest
# from app.core.security import get_password_hash

class NormCPFCService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_normcpfc_id(self, user_id: int, norm_id: int):
        return self.db.query(NormCPFC).filter(NormCPFC.UserID == user_id).filter(NormCPFC.NormID == norm_id).first()
    
    def get_normcpfc(self, user_id: int):
        return self.db.query(NormCPFC).filter(NormCPFC.UserID == user_id).all()
        
    def add_normcpfc(self, user_id: int, new_norm: NormCPFCRequest):

        inserted = NormCPFC(
            MinHeight=new_norm.MinHeight,
            MaxHeight=new_norm.MaxHeight,
            MinWeight=new_norm.MinWeight,
            MaxWeight=new_norm.MaxWeight,
            Calories=new_norm.Calories,
            Protein=new_norm.Protein,
            Fats=new_norm.Fats,
            Carbonatest=new_norm.Carbonatest,
            UserID=user_id
        )

        self.db.add(inserted)
        self.db.commit()

        return inserted
