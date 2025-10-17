from sqlalchemy import Column, ForeignKey, Integer, String
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from .usergoal import UserGoal

class NormCPFC(Base):
    __tablename__ = "normcpfc"
    
    NormID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    MinHeight: Mapped[int] = mapped_column(Integer)
    MaxHeight: Mapped[int] = mapped_column(Integer)
    MinWeight: Mapped[int] = mapped_column(Integer)
    MaxWeight: Mapped[int] = mapped_column(Integer)
    Calories: Mapped[int] = mapped_column(Integer)
    Protein: Mapped[int] = mapped_column(Integer)
    Fats: Mapped[int] = mapped_column(Integer)
    Carbonatest: Mapped[int] = mapped_column(Integer)

    GoalID: Mapped[int] = mapped_column(ForeignKey("usergoal.GoalID"))
    Goal: Mapped["UserGoal"] = relationship(back_populates="NormCPFC")