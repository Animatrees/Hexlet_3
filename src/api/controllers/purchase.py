from dataclasses import asdict

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, status

from src.api.dtos.purchase import (
    SuccessResponse,
    CreatePurchaseRequestDTO,
    PurchaseResponseDTO,
)
from src.apps.purchase import (
    CreatePurchaseInteractor,
    PurchaseInputDTO,
    GetAllPurchasesInteractor,
    PurchaseId,
    GetPurchaseInteractor,
    DeletePurchaseInteractor,
)

purchase_router = APIRouter(route_class=DishkaRoute)


@purchase_router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=SuccessResponse
)
async def create_purchase(
        dto: CreatePurchaseRequestDTO, interactor: FromDishka[CreatePurchaseInteractor]
) -> SuccessResponse:
    purchase = PurchaseInputDTO(**dto.model_dump())
    await interactor.execute(dto=purchase)
    return SuccessResponse(status='purchases_added')


@purchase_router.get('/', status_code=status.HTTP_200_OK, response_model=list[PurchaseResponseDTO])
async def get_purchases(interactor: FromDishka[GetAllPurchasesInteractor]) -> list[PurchaseResponseDTO]:
    purchases = await interactor.execute()
    return [PurchaseResponseDTO(**asdict(purchase)) for purchase in purchases] if purchases else []


@purchase_router.get(
    '/{purchase_id}',
    status_code=status.HTTP_200_OK,
    response_model=PurchaseResponseDTO,
)
async def get_purchase_by_id(
        purchase_id: PurchaseId,
        interactor: FromDishka[GetPurchaseInteractor],
) -> PurchaseResponseDTO:
    purchase = await interactor.execute(purchase_id=purchase_id)
    return PurchaseResponseDTO(**asdict(purchase))


@purchase_router.delete('/{purchase_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_purchase(
        purchase_id: PurchaseId,
        interactor: FromDishka[DeletePurchaseInteractor],
) -> None:
    await interactor.execute(purchase_id=purchase_id)
