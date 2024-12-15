from typing import Any, Tuple

from src.apps import ApplicationException
from src.apps.recommendation.entity import UserId


class RecoError(ApplicationException):
    DEFAULT_MESSAGE = 'Ошибка во время работы с рекомендациями.'

    def __init__(self, context: Exception = None, message: str = None) -> None:
        self.context = context
        self.message = message or self.DEFAULT_MESSAGE
        self.args: Tuple[Any, ...] = (self.context, self.message)

    def __str__(self) -> str:
        if self.context:
            return f'{self.message} {self.context}'

        return self.message


class RecoGenerateError(RecoError):
    DEFAULT_MESSAGE = 'Ошибка во время генерации рекомендаций.'


class RecoDoesNotExistError(RecoError):
    DEFAULT_MESSAGE = 'Рекомендации не найдены.'

    def __init__(
            self, user_id: UserId = None, context: Exception = None, message: str = None
    ) -> None:
        custom_message = f'Нет рекомендаций для пользователя с ID {user_id}.' if user_id else message
        super().__init__(context=context, message=custom_message or self.DEFAULT_MESSAGE)
        self.user_id = user_id
        self.args = (self.user_id, self.context, self.message)


class RepositoryError(RecoError):
    DEFAULT_MESSAGE = 'Ошибка репозитория.'
