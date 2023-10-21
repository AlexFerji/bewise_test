from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from .services import create_quiz


quiz_router = APIRouter(tags=['Quiz'])


@quiz_router.post('/test/')
async def quiz(session: AsyncSession = Depends(get_async_session)):

        result = await create_quiz(session=session)

        return result
