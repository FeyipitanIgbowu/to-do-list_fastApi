
from typing import List
from src.model.todo import Todo

class TodoRepository:
    def __init__(self):
        self.todos: List[Todo] = []

    def find_all(self):
        return self.todos

    def save(self, todo: Todo):
        self.todos.append(todo)
        return todo

    def find_by_id(self, todo_id: int):
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def delete(self, todo: Todo):
        self.todos.remove(todo)
