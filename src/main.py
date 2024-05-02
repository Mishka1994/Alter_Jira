from typing import Union
from fastapi import FastAPI
from config.settings import AppSettings
from src.api.person import person_router
from src.api.task import task_router

from src.config.db import Base

app = FastAPI(**AppSettings().model_dump())

app.include_router(person_router)
app.include_router(task_router)


@app.on_event('startup')
async def startup_event():
    from src.config.db import engine
    from src.model.task import Task # noqa
    from src.model.person import Person # noqa
    Base.metadata.create_all(bind=engine)

