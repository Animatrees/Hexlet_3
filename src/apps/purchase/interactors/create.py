from src.apps.purchase.mapper import PurchaseMapper
from src.apps.purchase.exceptions import PurchaseCreateError, RepositoryError
from src.apps.purchase.dtos import PurchaseInputDTO
from src.apps.purchase.interactors.base_interactor import BaseInteractor


class CreatePurchaseInteractor(BaseInteractor):
    async def execute(self, dto: PurchaseInputDTO) -> None:
        try:
            purchase = PurchaseMapper.dto_to_entity(dto=dto)
        except ValueError as e:
            raise PurchaseCreateError(context=e) from None

        try:
            await self._repository.save(purchase=purchase)
        except RepositoryError as e:
            raise PurchaseCreateError(context=e) from None
