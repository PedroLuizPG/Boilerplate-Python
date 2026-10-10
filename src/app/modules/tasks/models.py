from datetime import datetime

from sqlalchemy import DateTime,String,func,text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    done: Mapped[bool] = mapped_column(default=False, 
                                       server_default=text("false")
                                       )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )