from enum import Enum

from sqlalchemy import Column, Integer, String, Enum as EnumType
from sqlalchemy.orm import Mapped, relationship

from src.config.db import Base


class TaskStatus(str, Enum):
    todo = 'todo'
    in_progress = 'in_progress'
    done = 'done'


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(EnumType(TaskStatus), nullable=False)

    person_id = Column(Integer, nullable=False)
    person = relationship('Person', back_populates='task')

