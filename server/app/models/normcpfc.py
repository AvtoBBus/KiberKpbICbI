from sqlalchemy import Column, ForeignKey, Double, String, Double
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped


class NormCPFC(Base):
    __tablename__ = "normcpfc"
    
    NormID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    Weight: Mapped[Double] = mapped_column(Double)
    Height: Mapped[Double] = mapped_column(Double)
    DesiredWeight: Mapped[Double] = mapped_column(Double)

    Calories: Mapped[Double] = mapped_column(Double)
    Protein: Mapped[Double] = mapped_column(Double)
    Fats: Mapped[Double] = mapped_column(Double)
    Carbonatest: Mapped[Double] = mapped_column(Double)

    UserID: Mapped[int] = mapped_column(ForeignKey("user.UserID"))