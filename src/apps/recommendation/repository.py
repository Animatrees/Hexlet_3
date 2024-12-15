from abc import ABC, abstractmethod

from src.apps.recommendation.entity import RecoEntity, UserId


class IRecoRepository(ABC):

    @abstractmethod
    async def generate(self, user_id: UserId) -> None:
        pass

    @abstractmethod
    async def get_for_user(self, user_id: UserId) -> RecoEntity | None:
        pass
