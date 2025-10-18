from sqlalchemy.orm import Session
from app.models.normcpfc import NormCPFC
# from app.core.security import get_password_hash

class NormCPFCService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_normcpfc_id(self, norm_id: int):
        return self.db.query(NormCPFC).filter(NormCPFC.NormID == norm_id).first()
    
    def get_normcpfc(self):
        return self.db.query(NormCPFC).all()