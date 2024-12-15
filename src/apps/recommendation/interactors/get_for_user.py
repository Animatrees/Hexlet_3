from src.apps.recommendation.dtos import RecoOutputDTO
from src.apps.recommendation.entity import UserId
from src.apps.recommendation.exceptions import RecoDoesNotExistError
from src.apps.recommendation.interactors.base_interactor import BaseInteractor
from src.apps.recommendation.mapper import RecoMapper


class GetRecoForUserInteractor(BaseInteractor):
    async def execute(self, user_id: UserId) -> RecoOutputDTO:
        reco = await self._repository.get_for_user(user_id=user_id)
        if not reco:
            raise RecoDoesNotExistError(user_id=user_id)

        reco_dto = RecoMapper.entity_to_dto(entity=reco)
        return reco_dto
