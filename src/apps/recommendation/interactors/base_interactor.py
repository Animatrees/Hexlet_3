from abc import ABC, abstractmethod
from typing import Any

from src.apps.recommendation.repository import IRecoRepository


class BaseInteractor(ABC):
    def __init__(self, reco_repository: IRecoRepository):
        self._repository = reco_repository

    @abstractmethod
    async def execute(self, *args: Any) -> Any: ...
