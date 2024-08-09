from sqlalchemy import (
    Integer, ForeignKey, NUMERIC, String, TIMESTAMP
)
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column, relationship
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    second_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(70))
    phone_number: Mapped[str] = mapped_column(String(13))
    password: Mapped[str] = mapped_column(String(32))
    updated_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(50), nullable=True)
    date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True))
    deliver_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True))
    picup_point_id: Mapped[int] = mapped_column(ForeignKey("picup_point.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))


class OrderProduct(Base):
    __tablename__ = "order_product"

    order_id: Mapped[int] = mapped_column(
        ForeignKey("order.id"), primary_key=True
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("product.id"), primary_key=True
    )
    cnt: Mapped[int] = mapped_column(Integer())


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[NUMERIC] = mapped_column(NUMERIC(precision=10, scale=2))
    in_stock: Mapped[int] = mapped_column(Integer())
    description: Mapped[str] = mapped_column(String())
    photo: Mapped[str] = mapped_column(String())
    product_type_id: Mapped[int] = mapped_column(ForeignKey("product_type.id"))
    manufacturer_id: Mapped[int] = mapped_column(ForeignKey("manufacturer.id"))
    feedbacks: Mapped[list["Feedback"]] = relationship()


class Manufacturer(Base):
    __tablename__ = "manufacturer"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))


class ProductType(Base):
    __tablename__ = "product_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))


class PicupPoint(Base):
    __tablename__ = "picup_point"

    id: Mapped[int] = mapped_column(primary_key=True)
    physical_address: Mapped[str] = mapped_column(String(100))


class Feedback(Base):
    __tablename__ = "feedback"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    rate: Mapped[int] = mapped_column(Integer())
    text: Mapped[str] = mapped_column(String(), nullable=True)
