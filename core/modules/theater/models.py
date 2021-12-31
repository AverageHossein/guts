from sqlalchemy.orm import backref
from core.extensions import db
from sqlalchemy import Column, String, Integer
from core.utils.base_model import BaseModel

class Section(db.Model, BaseModel):
    __tablename__ = "section"

    name = Column(String(), nullable=False, unique=True)


class Seat(db.Model, BaseModel):
    __tablename__ = "seat"

    seat_number = Column(Integer(), nullable=False)
    row_number = Column(Integer(), nullable=False)
    rank = Column(Integer(), nullable=False)
    reserved_by = Column(Integer(), nullable=True)
    theater_id = Column(Integer, db.ForeignKey('theater.id'))
    section_id = Column(Integer, db.ForeignKey('section.id'))
    

class Theater(db.Model, BaseModel):
    __tablename__ = "theater"

    name = Column(String(), nullable=False)
    seats = db.relationship("Seat", backref=backref('theater', lazy='noload'))
