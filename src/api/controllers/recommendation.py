from dataclasses import asdict

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, status

from src.apps.recommendation import GenerateRecoInteractor, GetRecoForUserInteractor, UserId
from src.api.dtos.recommendation import SuccessResponse, RecoResponseDTO

reco_router = APIRouter(route_class=DishkaRoute)


@reco_router.post(
    '/generate/',
    status_code=status.HTTP_201_CREATED,
    response_model=SuccessResponse
)
async def generate_reco(
        user_id: UserId, interactor: FromDishka[GenerateRecoInteractor]
) -> SuccessResponse:
    await interactor.execute(user_id=user_id)
    return SuccessResponse(status='recommendations_generation_started')


@reco_router.get(
    '/{user_id}',
    status_code=status.HTTP_200_OK,
    response_model=RecoResponseDTO,
)
async def get_reco_for_user(
        user_id: UserId,
        interactor: FromDishka[GetRecoForUserInteractor],
) -> RecoResponseDTO:
    reco = await interactor.execute(user_id=user_id)
    return RecoResponseDTO(**asdict(reco))
