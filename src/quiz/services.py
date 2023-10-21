import requests
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.quiz.models import Quiz


async def create_quiz(session: AsyncSession):

        GET_QUIZ = requests.get('https://jservice.io/api/random?count=1')

        if GET_QUIZ.status_code == 200:
            data = GET_QUIZ.json()
            quiz_data = data[0]

            new_quiz = Quiz(id=quiz_data['id'],
                            answer=quiz_data['answer'],
                            question=quiz_data['question'],
                            airdate=quiz_data['airdate'],
                            created_at=quiz_data['created_at'],
                            updated_at=quiz_data['updated_at'],
                            category_id=quiz_data['category_id'],
                            game_id=quiz_data['game_id'])

            quiz_id = quiz_data['id']
            duplicate_quiz = await session.get(Quiz, quiz_id)
            get_quiz = await session.execute(select(Quiz))
            result = get_quiz.scalars().all()
            res = []

            if not duplicate_quiz:
                session.add(new_quiz)
                await session.commit()
            else:

                session.refresh(new_quiz)
                session.add(new_quiz)
                await session.commit()
            if not result:
                return res
            return result[-1]