from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import Column, ForeignKey, func, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as SQL_UUID

from src.data_access.models import Base

if TYPE_CHECKING:
    from . import ProductModel, UserModel


class ProductPurchaseModel(Base):
    __tablename__ = 'product_purchase'

    product_id = Column(ForeignKey('products.id', ondelete='CASCADE'), primary_key=True)
    purchase_id = Column(ForeignKey('purchases.id', ondelete='CASCADE'), primary_key=True)


class PurchaseModel(Base):
    __tablename__ = 'purchases'

    id: Mapped[UUID] = mapped_column(
        SQL_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        server_default=func.uuid_generate_v4(),
    )
    user_id: Mapped[UUID] = mapped_column(
        SQL_UUID(as_uuid=True),
        ForeignKey('users.id', ondelete='cascade')
    )
    purchase_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))

    user: Mapped['UserModel'] = relationship(
        back_populates='purchases',
    )

    products: Mapped[list['ProductModel']] = relationship(
        secondary='product_purchase',
        back_populates='purchases',
        passive_deletes=True,
    )
