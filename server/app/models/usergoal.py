from sqlalchemy import Column, ForeignKey, Integer, String
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped

class UserGoal(Base):
    __tablename__ = "usergoal"
    
    GoalID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Name: Mapped[str] = mapped_column(String)
    Description: Mapped[str] = mapped_column(String)

    NormCPFC: Mapped[list["NormCPFC"]] = relationship(back_populates="Goal")