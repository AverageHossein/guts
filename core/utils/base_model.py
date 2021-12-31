from sqlalchemy import Column, Integer, DateTime
import datetime as dt


class BaseModel(object):
    id = Column(Integer(), primary_key=True)
    created_at = Column(DateTime(), nullable=False, unique=False, default=dt.datetime.utcnow)
