from abc import ABC, abstractmethod
from typing import Any

from src.apps.purchase.repository import IPurchaseRepository


class BaseInteractor(ABC):
    def __init__(self, purchase_repository: IPurchaseRepository):
        self._repository = purchase_repository

    @abstractmethod
    async def execute(self, *args: Any) -> Any: ...
