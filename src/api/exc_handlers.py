from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.apps import ApplicationException
from src.apps.recommendation import RecoGenerateError, RecoDoesNotExistError
from src.apps.purchase.exceptions import (
    PurchaseCreateError, PurchaseDeleteError, PurchaseDoesNotExistError,

)

__all__ = ('init_exception_handlers',)

exception_status_codes = {
    PurchaseCreateError: status.HTTP_400_BAD_REQUEST,
    PurchaseDeleteError: status.HTTP_400_BAD_REQUEST,
    PurchaseDoesNotExistError: status.HTTP_404_NOT_FOUND,
    RecoGenerateError: status.HTTP_400_BAD_REQUEST,
    RecoDoesNotExistError: status.HTTP_404_NOT_FOUND,
    ApplicationException: status.HTTP_500_INTERNAL_SERVER_ERROR,
}


async def exception_handler(request: Request, exc: Exception) -> JSONResponse:
    if isinstance(exc, tuple(exception_status_codes.keys())):
        status_code = exception_status_codes[type(exc)]
        return JSONResponse(
            status_code=status_code,
            content={'message': str(exc)},
        )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={'message': 'Internal Server Error'},
    )


def init_exception_handlers(app: FastAPI) -> None:
    for exc_class in exception_status_codes:
        app.add_exception_handler(exc_class, exception_handler)
    app.add_exception_handler(Exception, exception_handler)
