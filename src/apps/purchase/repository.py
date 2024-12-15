from abc import ABC, abstractmethod

from src.apps.purchase.entity import PurchaseEntity, PurchaseId


class IPurchaseRepository(ABC):

    @abstractmethod
    async def save(self, purchase: PurchaseEntity) -> None:
        pass

    @abstractmethod
    async def get_by_id(self, purchase_id: PurchaseId) -> PurchaseEntity | None:
        pass

    @abstractmethod
    async def delete(self, purchase_id: PurchaseId) -> None:
        pass

    @abstractmethod
    async def get_list(self) -> list[tuple[PurchaseId, PurchaseEntity]]:
        pass
