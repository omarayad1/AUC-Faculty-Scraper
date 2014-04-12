from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_faculty_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Faculty(DeclarativeBase):
    __tablename__ = "faculty"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    department = Column('department', String, nullable=True)
    title = Column('title', String, nullable=True)
    email = Column('email', String, nullable=True)
    phone = Column('phone', String, nullable=True)
    building = Column('building', String, nullable=True)
    room = Column('room', String, nullable=True)
    campus = Column('campus', String, nullable=True)
