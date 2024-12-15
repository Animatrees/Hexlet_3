from pydantic import BaseModel, ConfigDict

from src.apps.recommendation import UserId, ProductId


class SuccessResponse(BaseModel):
    status: str


class RecoResponseDTO(BaseModel):
    user_id: UserId
    product: ProductId
    model_config = ConfigDict(
        from_attributes=True,
    )
