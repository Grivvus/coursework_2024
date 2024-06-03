import sqlalchemy
from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

user = "postgres"
password = "hackme"  # improve secrest managment
db_name = "postgres"
db_url = "0.0.0.0"
sqlalchemy_url = f"postgresql+psycopg2://{user}:{password}"\
  + "@{db_url}/{db_name}"


def create_db_engine(
    sqlalchemy_url: str
) -> Engine:
    return create_engine(sqlalchemy_url, echo=True)


def create_session(
    sqlalchemy_url: str = sqlalchemy_url
) -> Session:
    return Session(create_db_engine(sqlalchemy_url))
