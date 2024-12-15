from src.apps.purchase import PurchaseEntity, ProductId, UserId
from src.data_access.models import PurchaseModel


class PurchaseMapper:

    @staticmethod
    async def map_entity_to_model(entity: PurchaseEntity) -> PurchaseModel:
        model = PurchaseModel(
            user_id=entity.user_id,
            purchase_date=entity.purchase_date,
        )
        return model

    @staticmethod
    def map_model_to_entity(model: PurchaseModel) -> PurchaseEntity:
        purchase = PurchaseEntity(
            user_id=UserId(model.user_id),
            products=[ProductId(product.id) for product in model.products]
        )
        purchase.purchase_date = model.purchase_date
        return purchase
