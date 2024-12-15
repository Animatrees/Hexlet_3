from typing import Any, Tuple

from src.apps import ApplicationException
from src.apps.purchase.entity import PurchaseId


class PurchaseError(ApplicationException):
    DEFAULT_MESSAGE = 'Ошибка во время работы с покупкой.'

    def __init__(self, context: Exception = None, message: str = None) -> None:
        self.context = context
        self.message = message or self.DEFAULT_MESSAGE
        self.args: Tuple[Any, ...] = (self.context, self.message)

    def __str__(self) -> str:
        if self.context:
            return f'{self.message} {self.context}'

        return self.message


class PurchaseCreateError(PurchaseError):
    DEFAULT_MESSAGE = 'Ошибка во время создания покупки.'


class PurchaseDeleteError(PurchaseError):
    DEFAULT_MESSAGE = 'Ошибка во время удаления покупки.'


class PurchaseDoesNotExistError(PurchaseError):
    DEFAULT_MESSAGE = 'Покупка не найдена.'

    def __init__(
        self, purchase_id: PurchaseId = None, context: Exception = None, message: str = None
    ) -> None:
        custom_message = f'Покупка с ID {purchase_id} не найдена.' if purchase_id else message
        super().__init__(context=context, message=custom_message or self.DEFAULT_MESSAGE)
        self.purchase_id = purchase_id
        self.args = (self.purchase_id, self.context, self.message)


class RepositoryError(PurchaseError):
    DEFAULT_MESSAGE = 'Ошибка репозитория.'
