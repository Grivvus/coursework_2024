from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user" 
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    second_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(70))
    phone_number: Mapped[str] = mapped_column(String(13))
    password: Mapped[str] = mapped_column(String(32)) # for md5 hash algorithm
    is_super_user: Mapped[bool] = mapped_column(Boolean())

class Order(Base):
    __tablename__ = "order"


class Product(Base):
    __tablename__ = "product"


class Manufacturer(Base):
    __tablename__ = "manufacturer"


class ProductType(Base):
    __tablename__ = "product_type"


class PicupPoint(Base):
    __tablename__ = "picup_point"


class Feedback(Base):
    __tablename__ = "feedback"

