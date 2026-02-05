from src.repository.todo_repository import TodoRepository
from src.model.todo import Todo

class TodoService:

    def __init__(self, repo: TodoRepository):
        self.repo = repo

    def get_todos(self, db):
        return self.repo.find_all(db)

    def create_todo(self, db, title: str):
        todo = Todo(title=title)
        return self.repo.save(db, todo)

    def complete_todo(self, db, todo_id: int):
        todo = self.repo.find_by_id(db, todo_id)
        if not todo:
            return None
        todo.completed = True
        return self.repo.save(db, todo)

    def delete_todo(self, db, todo_id: int):
        todo = self.repo.find_by_id(db, todo_id)
        if not todo:
            return None
        self.repo.delete(db, todo)
        return todo
