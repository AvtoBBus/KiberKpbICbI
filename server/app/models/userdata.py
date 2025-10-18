from sqlalchemy import Column, ForeignKey, Integer, String
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from .normcpfc import NormCPFC

class UserData(Base):
    __tablename__ = "userdata"
    
    UserDataID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Height: Mapped[int] = mapped_column(Integer)
    Weight: Mapped[int] = mapped_column(Integer)
    Age: Mapped[int] = mapped_column(Integer)
    
    UserID: Mapped[int] = mapped_column(ForeignKey("user.UserID"))

    NormID: Mapped[int] = mapped_column(ForeignKey("normcpfc.NormID"))
    Norm: Mapped["NormCPFC"] = relationship(back_populates="UserData")