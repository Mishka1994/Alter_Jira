from enum import Enum

from pydantic import BaseModel, ConfigDict


class BaseTaskStruct(BaseModel):
    title: str
    description: str
    status: Enum

    model_config = ConfigDict(from_attributes=True)


class CreateTaskStruct(BaseTaskStruct):
    pass


class UpdateTaskStruct(BaseTaskStruct):
    pass


class TaskStruct(BaseTaskStruct):
    id: int
