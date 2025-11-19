from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from app.utils.db import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped

from typing import Literal, get_args

class UserData(Base):
    __tablename__ = "userdata"
    
    UserDataID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    UserName: Mapped[str] = mapped_column(String)
    Activity: Mapped[int] = mapped_column(Integer)
    Age: Mapped[int] = mapped_column(Integer)
    Gender: Mapped[Literal['м', 'ж']] = mapped_column(Enum(*get_args(Literal['м', 'ж'])))
    Height: Mapped[int] = mapped_column(Integer)
    Weight: Mapped[int] = mapped_column(Integer)
    DesiredHeight: Mapped[int] = mapped_column(Integer)
    DesiredWeight: Mapped[int] = mapped_column(Integer)
    
    UserID: Mapped[int] = mapped_column(ForeignKey("user.UserID"))