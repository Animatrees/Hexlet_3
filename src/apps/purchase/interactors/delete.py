from src.apps.purchase.entity import PurchaseId
from src.apps.purchase.exceptions import RepositoryError, PurchaseDeleteError
from src.apps.purchase.interactors.base_interactor import BaseInteractor


class DeletePurchaseInteractor(BaseInteractor):
    async def execute(self, purchase_id: PurchaseId) -> None:
        try:
            await self._repository.delete(purchase_id=purchase_id)
        except RepositoryError as e:
            raise PurchaseDeleteError(context=e) from None
