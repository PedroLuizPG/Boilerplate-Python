from collections.abc import Sequence
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.tasks.models import Task
from app.modules.tasks.repository import TaskRepository


class SqlAlchemyTaskRepository(TaskRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        
    async def list_all(self) -> Sequence[Task]:
        result = await self._session.scalars(select(Task).order_by(Task.id.desc()))
        return result.all()
    
    async def get_by_id(self, task_id: int) -> Task | None:
        return await self._session.get(Task, task_id)
    
    async def add(self, title: str) -> Task:
        task = Task(title=title)
        self._session.add(task)
        
        await self._session.commit()
        
        # garante os valores gerados pelo banco (id, created_at)
        await self._session.refresh(task)
        return task
    
    async def update(self, task: Task, values: dict[str, Any]) -> Task:
        for field, value in values.items():
            setattr(task, field, value)
            
        await self._session.commit()
        await self._session.refresh(task)
        
        return task
    
    async def delete(self, task: Task) -> None:
        await self._session.delete(Task)
        await self._session.commit()