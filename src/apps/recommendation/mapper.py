from src.apps.recommendation.dtos import RecoOutputDTO
from src.apps.recommendation.entity import RecoEntity


class RecoMapper:

    @staticmethod
    def entity_to_dto(
            entity: RecoEntity,
    ) -> RecoOutputDTO:
        return RecoOutputDTO(
            user_id=entity.user_id,
            product=entity.product
        )
