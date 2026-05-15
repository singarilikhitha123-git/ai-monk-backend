from sqlalchemy import Column, Integer, JSON, DateTime
from sqlalchemy.sql import func
from database import Base


class Tree(Base):
    __tablename__ = "trees"

    id = Column(Integer, primary_key=True, index=True)
    tree = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
