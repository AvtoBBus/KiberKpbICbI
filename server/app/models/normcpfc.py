from sqlalchemy import Column, ForeignKey, Integer, String
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped


class NormCPFC(Base):
    __tablename__ = "normcpfc"
    
    NormID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    Weight: Mapped[int] = mapped_column(Integer)
    Height: Mapped[int] = mapped_column(Integer)
    DesiredWeight: Mapped[int] = mapped_column(Integer)

    Calories: Mapped[int] = mapped_column(Integer)
    Protein: Mapped[int] = mapped_column(Integer)
    Fats: Mapped[int] = mapped_column(Integer)
    Carbonatest: Mapped[int] = mapped_column(Integer)

    UserID: Mapped[int] = mapped_column(ForeignKey("user.UserID"))