from fastapi import FastAPI
from src.routes.todo_route import router as todo_router

app = FastAPI(title="Todo")
app.include_router(todo_router)
