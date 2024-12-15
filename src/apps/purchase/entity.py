from datetime import datetime, timezone
from typing import NewType
from uuid import UUID

PurchaseId = NewType('PurchaseId', UUID)
UserId = NewType('UserId', UUID)
ProductId = NewType('ProductId', UUID)


class PurchaseEntity:
    def __init__(
            self,
            user_id: UserId,
            products: list[ProductId]
    ) -> None:
        self.user_id = user_id
        self.purchase_date = datetime.now(timezone.utc)
        self.products = products
