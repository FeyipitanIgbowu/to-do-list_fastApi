from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.db import SessionLocal
from src.repository.todo_repository import TodoRepository
from src.services.todo_service import TodoService
from src.schemas.todo_schema import TodoCreate, TodoResponse

router = APIRouter(prefix="/todos", tags=["Todos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

service = TodoService(TodoRepository())

@router.get("", response_model=list[TodoResponse])
def get_todos(db: Session = Depends(get_db)):
    return service.get_todos(db)

@router.post("", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return service.create_todo(db, todo.title)

@router.put("/{todo_id}", response_model=TodoResponse)
def complete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = service.complete_todo(db, todo_id)
    if not todo:
        raise HTTPException(404, "Todo not found")
    return todo

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = service.delete_todo(db, todo_id)
    if not todo:
        raise HTTPException(404, "Todo not found")
    return {"message": "Todo deleted"}
