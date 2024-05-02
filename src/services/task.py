from src.model.task import Task
from src.structs.task import TaskStruct, CreateTaskStruct, UpdateTaskStruct


class TaskService:

    @classmethod
    def get_task_by_id(cls, task_id: int, db) -> TaskStruct:
        query = db.qyery(Task).filter(Task.id == task_id).first()
        data = TaskStruct.model_validate(query)
        return data

    @classmethod
    def get_all_task(cls, db) -> list[TaskStruct]:
        query = db.qyery(Task).all()
        data = [TaskStruct.model_validate(el) for el in query]
        return data

    @classmethod
    def create_task(cls, data: CreateTaskStruct, db) -> TaskStruct:
        task = Task(**data.model_dump())
        db.add(task)
        db.commit()
        db.refresh(task)
        return TaskStruct.model_validate(task)

    @classmethod
    def update_task(cls, task_id: int, data: UpdateTaskStruct, db) -> TaskStruct:
        task = db.query(Task).filter(Task.id == task_id).first()
        for key, value in data.dict().items():
            setattr(task, key,value)
        db.commit()
        db.refresh(task)
        return TaskStruct.model_validate(task)

    @classmethod
    def delete_task(cls, task_id: int, db):
        db.query(Task).filter(Task.id == task_id).delete()
        db.commit()
        return {'message': 'Task deleted successfully'}
