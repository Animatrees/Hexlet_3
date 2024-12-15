from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

from src.config import DbConfig as db


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=db.naming_convention)
