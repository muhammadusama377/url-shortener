from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String, unique=True, index=True)
    url = Column(String)
    expired = Column(Boolean, default=False)
