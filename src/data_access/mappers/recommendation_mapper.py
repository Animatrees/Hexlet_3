from src.apps.recommendation import RecoEntity, ProductId, UserId
from src.data_access.models import RecoModel


class RecoMapper:

    @staticmethod
    def model_to_entity(model: RecoModel) -> RecoEntity:
        reco = RecoEntity(
            user_id=UserId(model.user_id),
            product=ProductId(model.product_id)
        )
        return reco
