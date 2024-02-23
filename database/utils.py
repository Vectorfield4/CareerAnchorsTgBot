
from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from database import User, Result


async def save_user(session_maker:sessionmaker, user:User):
    async with session_maker() as session:
        async with session.begin():
            session: AsyncSession
            await session.merge(user)

async def update_user_result(session_maker:sessionmaker, result:Result):
    async with session_maker() as session:
        async with session.begin():
            session: AsyncSession
            result_to_update = await session.execute(select(Result).where(Result.user_id == result.user_id))
            result_to_update = result_to_update.scalars().first()
            if result_to_update:
                result_to_update.answers = result.answers
                result_to_update.finished = result.finished
                result_to_update.updated = result.updated
                await session.commit()
            else:
                await session.merge(result)