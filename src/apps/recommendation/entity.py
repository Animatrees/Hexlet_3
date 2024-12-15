from typing import NewType
from uuid import UUID

RecoId = NewType('RecoId', UUID)
UserId = NewType('UserId', UUID)
ProductId = NewType('ProductId', UUID)


class RecoEntity:
    def __init__(
            self,
            user_id: UserId,
            product: ProductId
    ) -> None:
        self.user_id = user_id
        self.product = product
