from fastapi import APIRouter
from repository import TaskRepository
from schemas import STaskAdd, STaskId
from fastapi import APIRouter, Depends
from typing import Annotated

router = APIRouter(
    prefix='/tasks',
    tags=['Таски'],
)

@router.post('')
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}


@router.get('')
async def get_tasks() -> list[STaskId]:
    tasks = await TaskRepository.find_all()
    return tasks
