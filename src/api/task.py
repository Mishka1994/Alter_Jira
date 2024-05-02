from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.config.db import get_db
from src.services.task import TaskService
from src.structs.task import TaskStruct, CreateTaskStruct, UpdateTaskStruct

task_router = APIRouter(prefix='/task', tags=['Task'])


@task_router.get('/')
def all_(db: Session = Depends(get_db)):
    return TaskService.get_all_task(db)


@task_router.get('/{task_id}')
def get(task_id: int, db: Session = Depends(get_db)) -> TaskStruct:
    return TaskService.get_task_by_id(task_id, db)


@task_router.post('/')
def create(task: CreateTaskStruct, db: Session = Depends(get_db)) -> TaskStruct:
    return TaskService.create_task(task, db)


@task_router.put('/{task_id}')
def update(task_id: int, data: UpdateTaskStruct, db: Session = Depends(get_db)) -> TaskStruct:
    return TaskService.update_task(task_id, data, db)


@task_router.delete('/')
def delete(task_id: int, db: Session = Depends(get_db)) -> TaskStruct:
    return TaskService.delete_task(task_id, db)
