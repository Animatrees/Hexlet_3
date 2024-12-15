from src.apps.recommendation import UserId
from src.apps.recommendation.exceptions import RecoGenerateError, RepositoryError
from src.apps.recommendation.interactors.base_interactor import BaseInteractor


class GenerateRecoInteractor(BaseInteractor):
    async def execute(self, user_id: UserId) -> None:
        try:
            await self._repository.generate(user_id=user_id)
        except RepositoryError as e:
            raise RecoGenerateError(context=e) from None
