from sqlalchemy.orm import Session
from src.model.todo import Todo

class TodoRepository:

    def find_all(self, db: Session):
        return db.query(Todo).all()

    def save(self, db: Session, todo: Todo):
        db.add(todo)
        db.commit()
        db.refresh(todo)
        return todo

    def find_by_id(self, db: Session, todo_id: int):
        return db.query(Todo).filter(Todo.id == todo_id).first()

    def delete(self, db: Session, todo: Todo):
        db.delete(todo)
        db.commit()
