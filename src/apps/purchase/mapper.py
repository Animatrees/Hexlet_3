from src.apps.purchase.dtos import PurchaseOutputDTO, PurchaseInputDTO
from src.apps.purchase.entity import PurchaseId, PurchaseEntity


class PurchaseMapper:

    @staticmethod
    def entity_to_dto(
            purchase_id: PurchaseId,
            entity: PurchaseEntity,
    ) -> PurchaseOutputDTO:
        return PurchaseOutputDTO(
            id=purchase_id,
            user_id=entity.user_id,
            purchase_date=entity.purchase_date,
            products=entity.products
        )

    @staticmethod
    def dto_to_entity(dto: PurchaseInputDTO) -> PurchaseEntity:
        return PurchaseEntity(
            user_id=dto.user_id,
            products=dto.products
        )
