from fastapi import FastAPI

from .purchase import purchase_router
from .health_check import router
from .recommendation import reco_router


def init_routes(app: FastAPI) -> None:
    prefix: str = '/api'
    app.include_router(
        router=router,
        prefix=f'{prefix}/health-check',
        tags=['Test'],
    )
    app.include_router(router=purchase_router, prefix=f'{prefix}/purchases', tags=['Purchase'])
    app.include_router(router=reco_router, prefix=f'{prefix}/recommendations', tags=['Recommendation'])


__all__ = ('init_routes',)
