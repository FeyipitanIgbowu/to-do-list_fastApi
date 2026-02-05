# This be where HTTP request dey land

from fastapi import APIRouter, HTTPException
from src.schemas.todo_schema import TodoCreate, TodoResponse
from src.services.todo_service import TodoService
from src.repository.todo_repository import TodoRepository

router = APIRouter(prefix="/todos", tags=["Chale Todos"])

repo = TodoRepository()
service = TodoService(repo)

@router.get("", response_model=list[TodoResponse])
def list_all():
    return service.list_todos()

@router.post("", response_model=TodoResponse)
def create(todo: TodoCreate):
    return service.add_todo(todo.title)

@router.put("/{todo_id}", response_model=TodoResponse)
def complete(todo_id: int):
    todo = service.mark_done(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Chale, todo no dey")
    return todo

@router.delete("/{todo_id}")
def delete(todo_id: int):
    todo = service.remove_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Ei, we no find am")
    return {"message": "Todo clear. Respect 👊"}
