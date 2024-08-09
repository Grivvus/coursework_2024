from typing import Generator

from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.settings import settings


sqlalchemy_url = f"postgresql+psycopg2://{settings.POSTGRES_USER}:"\
  + f"{settings.POSTGRES_PASSWORD}@0.0.0.0/{settings.POSTGRES_DB}"


def _create_db_engine() -> Engine:
    return create_engine(sqlalchemy_url, echo=True)


engine = _create_db_engine()


def create_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
