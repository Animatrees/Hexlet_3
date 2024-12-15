from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID as SQL_UUID

from src.data_access.models import Base

if TYPE_CHECKING:
    from . import PurchaseModel, RecoModel


class ProductModel(Base):
    __tablename__ = 'products'

    id: Mapped[UUID] = mapped_column(
        SQL_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        server_default=func.uuid_generate_v4(),
    )
    name: Mapped[str]
    category: Mapped[str]

    purchases: Mapped[list['PurchaseModel']] = relationship(
        secondary='product_purchase',
        back_populates='products',
        passive_deletes=True,
    )

    recommendations: Mapped[list['RecoModel']] = relationship('RecoModel', back_populates='product')
