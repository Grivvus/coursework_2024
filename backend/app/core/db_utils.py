from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.settings import settings


sqlalchemy_url = f"postgresql+psycopg2://{settings.POSTGRES_USER}:"\
  + f"{settings.POSTGRES_PASSWORD}@0.0.0.0/{settings.POSTGRES_DB}"


def create_db_engine(
    sqlalchemy_url: str = sqlalchemy_url
) -> Engine:
    return create_engine(sqlalchemy_url, echo=True)


def create_session(
    sqlalchemy_url: str = sqlalchemy_url
) -> Session:
    return Session(create_db_engine(sqlalchemy_url))
