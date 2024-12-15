from src.apps.purchase.dtos import PurchaseOutputDTO
from src.apps.purchase.entity import PurchaseId
from src.apps.purchase.exceptions import PurchaseDoesNotExistError
from src.apps.purchase.interactors.base_interactor import BaseInteractor
from src.apps.purchase.mapper import PurchaseMapper


class GetPurchaseInteractor(BaseInteractor):
    async def execute(self, purchase_id: PurchaseId) -> PurchaseOutputDTO:
        purchase = await self._repository.get_by_id(purchase_id=purchase_id)
        if not purchase:
            raise PurchaseDoesNotExistError(purchase_id)

        purchase_dto = PurchaseMapper.entity_to_dto(purchase_id=purchase_id, entity=purchase)
        return purchase_dto
