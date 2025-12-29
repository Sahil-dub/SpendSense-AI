from sqlalchemy import Column, Integer, String
from app.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    flexibility_level = Column(String, nullable=False)  # fixed | semi | flexible
    monthly_threshold = Column(Integer, default=0)
