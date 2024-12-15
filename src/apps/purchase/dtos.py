from dataclasses import dataclass
from datetime import datetime

from src.apps.purchase.entity import PurchaseId, UserId, ProductId


@dataclass
class PurchaseInputDTO:
    user_id: UserId
    products: list[ProductId]


@dataclass
class PurchaseOutputDTO:
    id: PurchaseId
    user_id: UserId
    purchase_date: datetime
    products: list[ProductId]
