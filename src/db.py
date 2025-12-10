from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError

from .models import Movie, Series


Base = declarative_base()


class MovieDB(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    year = Column(Integer)
    rating = Column(Float)


class SeriesDB(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    year = Column(Integer)
    seasons = Column(Integer)
    episodes = Column(Integer)


def get_engine(path="data/imdb.db"):
    return create_engine(f"sqlite:///{path}")


def create_tables(engine=None):
    if engine is None:
        engine = get_engine()
    Base.metadata.create_all(engine)


def get_session(engine=None):
    if engine is None:
        engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()


def insert_movies(movies, session):
    for m in movies:
        try:
            obj = MovieDB(title=m.title, year=m.year, rating=m.rating)
            session.add(obj)
            session.commit()
        except IntegrityError:
            session.rollback()
            print(f"[DUPLICADO] Filme ignorado: {m.title}")


def insert_series(series_list, session):
    for s in series_list:
        try:
            obj = SeriesDB(
                title=s.title,
                year=s.year,
                seasons=s.seasons,
                episodes=s.episodes,
            )
            session.add(obj)
            session.commit()
        except IntegrityError:
            session.rollback()
            print(f"[DUPLICADA] Série ignorada: {s.title}")
