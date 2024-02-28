from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router
from pydantic import BaseModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База данных очищена')
    await create_tables()
    print('База данных готова к работе')
    yield
    print('Выключение')

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)