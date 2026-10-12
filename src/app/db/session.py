from collections.abc import AsyncIterator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker,create_async_engine

from app.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, pool_pre_ping=True)

# expire_on_commit=False é importante no modo async: por padrão, após o commit
# o SQLAlchemy "expira" os atributos e tentaria recarregá-los sozinho (lazy load),
# o que não funciona em async e gera o erro MissingGreenlet.

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncIterator[AsyncSession]:
    """
    Uma sessão por request. O 'async with' garante o fechamento no final
    """
    
    async with SessionLocal() as session:
        yield session
        
SessionDep = Annotated[AsyncSession,Depends(get_session)]
    