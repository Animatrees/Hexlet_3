from datetime import datetime

from pydantic import BaseModel, ConfigDict

from src.apps.purchase import UserId, ProductId, PurchaseId


class SuccessResponse(BaseModel):
    status: str


class CreatePurchaseRequestDTO(BaseModel):
    user_id: UserId
    products: list[ProductId]


class PurchaseResponseDTO(BaseModel):
    id: PurchaseId
    user_id: UserId
    purchase_date: datetime
    products: list[ProductId]
    model_config = ConfigDict(
        from_attributes=True,
    )
