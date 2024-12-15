from dataclasses import dataclass

from src.apps.recommendation.entity import UserId, ProductId


@dataclass
class RecoOutputDTO:
    user_id: UserId
    product: ProductId
