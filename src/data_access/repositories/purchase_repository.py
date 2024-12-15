from asyncpg import ForeignKeyViolationError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.apps.purchase import IPurchaseRepository, ProductId, PurchaseId, PurchaseEntity, RepositoryError
from src.data_access.mappers.purchase_mapper import PurchaseMapper
from src.data_access.models import PurchaseModel, ProductModel


class PurchaseRepository(IPurchaseRepository):

    def __init__(self, session: AsyncSession):
        self._session = session
        self.model = PurchaseModel
        self.mapper = PurchaseMapper()

    async def _get_products(
            self,
            list_ids: list[ProductId],
    ) -> list[ProductModel]:
        query = select(ProductModel).where(ProductModel.id.in_(list_ids))
        result = await self._session.execute(query)
        products = result.scalars().all()
        return list(products)

    async def save(self, purchase: PurchaseEntity) -> None:
        purchase_model = await self.mapper.map_entity_to_model(purchase)
        purchase_model.products = await self._get_products(purchase.products)
        try:
            self._session.add(purchase_model)
            await self._session.flush()
        except IntegrityError as e:
            orig_exception = e.orig.__cause__
            if isinstance(orig_exception, ForeignKeyViolationError):
                detail_message = orig_exception.detail  # noqa
                raise RepositoryError(detail_message)
            else:
                raise

    async def get_by_id(self, purchase_id: PurchaseId) -> PurchaseEntity | None:
        stmt = (
            select(self.model)
            .where(self.model.id == purchase_id)
            .options(selectinload(self.model.products))
        )
        result = await self._session.execute(stmt)
        purchase_model = result.scalar_one_or_none()
        if purchase_model:
            return self.mapper.map_model_to_entity(purchase_model)
        else:
            return None

    async def delete(self, purchase_id: PurchaseId) -> None:
        purchase_model = await self._session.get(self.model, purchase_id)
        if purchase_model:
            await self._session.delete(purchase_model)
        else:
            raise RepositoryError(message=f'Не найдена покупка с id: {purchase_id}')

    async def get_list(self) -> list[tuple[PurchaseId, PurchaseEntity]] | None:
        stmt = (select(self.model).options(selectinload(self.model.products)))
        result = await self._session.execute(stmt)
        purchases = result.scalars().all()
        return (
            [(PurchaseId(purchase.id), self.mapper.map_model_to_entity(purchase)) for purchase in purchases]
            if purchases
            else None
        )
