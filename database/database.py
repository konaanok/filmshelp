
from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import Column, Float, ForeignKey, Integer, String

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB 


from database.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}" 

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user" 
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, nullable=False, primary_key=True)
    hashed_password = Column(String, nullable=False)


class Genre(Base):
    __tablename__ = "genres" 

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String, nullable=False) 

    directors = relationship("Director", secondary="genre_director", back_populates="genres")


class Director(Base):
    __tablename__ = "directors" 

    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String, nullable=False)  

    descriptions = relationship("Description", back_populates="director")
    genres = relationship("Genre", secondary="genre_director", back_populates="directors")


class Description(Base):
    __tablename__ = "descriptions"  

    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String, nullable=False)
    content = Column(String, nullable=False)  
    director_id = Column(Integer, ForeignKey('directors.id'))  

    director = relationship("Director", back_populates="descriptions")

class Film(Base):
    __tablename__ = "film" 

    id = Column(Integer, primary_key=True, index=True)  
    title = Column(String, nullable=False)  
    year = Column(Integer, nullable=False)  
    description_id = Column(Integer, ForeignKey('descriptions.id'))

    description = relationship("Description")

class Rating(Base):
    __tablename__ = "rating"
    id = Column(Integer, primary_key=True, autoincrement=True)
    rating_user = Column(Float, nullable=True)
    review = Column(JSONB, nullable=True)
    film_id = Column(Integer, ForeignKey('film.id'))
    username = Column(String, ForeignKey('user_username'))

    user = relationship("User")
    film = relationship("Film")

class RatingAverage(Base):
    __tablename__ = "rating_average"
    rating_average = Column(Float, default=0.0)
    rating_count = Column(Integer, default=0)
    rating_web = Column(Float)
    film_id = Column(Integer, ForeignKey("film.id", ondelete="CASCADE"), primary_key=True)
    film = relationship("Film")


engine = create_async_engine(DATABASE_URL) 
async_session_maker = async_sessionmaker(engine, expire_on_commit=False) 

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    return session

async def get_film_db(session: AsyncSession = Depends(get_async_session)):
    return session



