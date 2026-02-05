
from src.repository.todo_repository import TodoRepository
from src.model.todo import Todo

class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def list_todos(self):
        return self.repository.find_all()

    def add_todo(self, title: str):
        todo = Todo(
            id=len(self.repository.find_all()) + 1,
            title=title
        )
        return self.repository.save(todo)

    def mark_done(self, todo_id: int):
        todo = self.repository.find_by_id(todo_id)
        if not todo:
            return None
        todo.completed = True
        return todo

    def remove_todo(self, todo_id: int):
        todo = self.repository.find_by_id(todo_id)
        if not todo:
            return None
        self.repository.delete(todo)
        return todo
