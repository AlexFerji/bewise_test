from sqlalchemy import MetaData, Column, Integer, String,Table

from src.database import Base


metadata = MetaData()

quiz = Table(
    'quiz',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('answer', String),
    Column('question', String),
    Column('airdate', String),
    Column('created_at', String),
    Column('updated_at', String),
    Column('category_id', Integer),
    Column('game_id', Integer),
)


class Quiz(Base):
    __tablename__ = 'quiz'

    id = Column(Integer, primary_key=True)
    answer = Column(String)
    question = Column(String)
    airdate = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    category_id = Column(Integer)
    game_id = Column(Integer)


