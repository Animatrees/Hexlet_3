from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as SQL_UUID

from src.data_access.models import Base

if TYPE_CHECKING:
    from . import ProductModel, UserModel


class RecoModel(Base):
    __tablename__ = 'recommendations'

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

    product_id: Mapped[UUID] = mapped_column(
        SQL_UUID(as_uuid=True),
        ForeignKey('products.id', ondelete='cascade')
    )

    user: Mapped['UserModel'] = relationship(
        back_populates='recommendations',
    )

    product: Mapped['ProductModel'] = relationship(
        back_populates='recommendations',
    )
