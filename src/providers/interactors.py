from dishka import Provider, Scope, provide

from src.apps.recommendation import GenerateRecoInteractor, GetRecoForUserInteractor
from src.apps.purchase import (
    CreatePurchaseInteractor,
    DeletePurchaseInteractor,
    GetAllPurchasesInteractor,
    GetPurchaseInteractor,
)


class PurchaseInteractorProvider(Provider):
    scope = Scope.REQUEST

    create_purchase = provide(CreatePurchaseInteractor)
    get_purchase_by_id = provide(GetPurchaseInteractor)
    get_purchases = provide(GetAllPurchasesInteractor)
    delete_purchase = provide(DeletePurchaseInteractor)


class RecoInteractorProvider(Provider):
    scope = Scope.REQUEST

    generate_reco = provide(GenerateRecoInteractor)
    get_purchase_for_user = provide(GetRecoForUserInteractor)
