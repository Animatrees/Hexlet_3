from src.apps.purchase.dtos import PurchaseOutputDTO
from src.apps.purchase.interactors.base_interactor import BaseInteractor
from src.apps.purchase.mapper import PurchaseMapper


class GetAllPurchasesInteractor(BaseInteractor):
    async def execute(self) -> list[PurchaseOutputDTO] | None:
        purchases = await self._repository.get_list()
        return (
            [PurchaseMapper.entity_to_dto(*purchase) for purchase in purchases] if purchases else None
        )
