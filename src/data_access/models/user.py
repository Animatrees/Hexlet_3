from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import func, String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy.dialects.postgresql import UUID as SQL_UUID

from src.data_access.models import Base

if TYPE_CHECKING:
    from data_access.models import PurchaseModel, RecoModel


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(
        SQL_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        server_default=func.uuid_generate_v4(),
    )
    username: Mapped[str]
    email: Mapped[str] = mapped_column(String(100), unique=True)

    purchases: Mapped[list['PurchaseModel']] = relationship('PurchaseModel', back_populates='user')
    recommendations: Mapped[list['RecoModel']] = relationship('RecoModel', back_populates='user')
