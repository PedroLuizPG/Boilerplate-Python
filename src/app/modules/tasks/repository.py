from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any

from app.modules.tasks.models import Task


class TaskRepository(ABC):
    """Contrato que o Service conhece. Qualquer classe que o cumprir pode ser plugada por baixo."""
    
    @abstractmethod
    async def list_all(self) -> Sequence[Task]: ...
    
    @abstractmethod
    async def get_by_id(self, task_id: int) -> Task | None: ...
    
    @abstractmethod
    async def add(self, title: str) -> Task: ...
    
    @abstractmethod
    async def update(self, task: Task, values: dict[str, Any]) -> Task: ...
    
    @abstractmethod
    async def delete(self, task: Task) -> None: ...
    
    
    