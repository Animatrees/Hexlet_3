from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
import pandas as pd

from src.apps.recommendation import UserId, RecoEntity
from src.data_access.mappers.recommendation_mapper import RecoMapper
from src.data_access.models import RecoModel, PurchaseModel, ProductModel
from src.apps.recommendation import IRecoRepository


class RecoRepository(IRecoRepository):

    def __init__(self, session: AsyncSession):
        self._session = session
        self.model = RecoModel
        self.mapper = RecoMapper()

    async def generate(self, user_id: UserId) -> None:
        # I tried so hard and got so far, but in the end, it doesn't even matter...))
        # В общем скрипт ниже написан полностью Клодом, поэтому я понятия не имею работает ли он корректно.
        # Не хватило времени, чтобы протестировать. Плак.
        # Но, вы можете посмотреть как реализовано применение Чистой архитектуры в проекте))


        # Step 1: Get all purchases with their products
        purchases = await self._session.execute(
            select(PurchaseModel.id, PurchaseModel.user_id, ProductModel.id.label('product_id'))
            .join(PurchaseModel.products)
        )
        purchases_df = pd.DataFrame(purchases.fetchall(), columns=['purchase_id', 'user_id', 'product_id'])

        # Step 2: Create co-purchase matrix
        user_product_matrix = pd.pivot_table(purchases_df, values='purchase_id', index='user_id', columns='product_id', aggfunc='count', fill_value=0)
        co_purchase_matrix = user_product_matrix.T.dot(user_product_matrix)

        # Step 3: Get user's purchase history
        user_purchases = await self._session.execute(
            select(ProductModel.id)
            .join(PurchaseModel.products)
            .where(PurchaseModel.user_id == user_id)
        )
        user_products = [row[0] for row in user_purchases.fetchall()]

        # Step 4: Find products not in user's history with highest co-purchase frequency
        recommendations = co_purchase_matrix.loc[user_products].sum().sort_values(ascending=False)
        recommendations = recommendations[~recommendations.index.isin(user_products)]

        if not recommendations.empty:
            # Step 5: Get product popularity
            product_popularity = await self._session.execute(
                select(ProductModel.id, func.count(PurchaseModel.id).label('popularity'))
                .join(PurchaseModel.products)
                .group_by(ProductModel.id)
            )
            popularity_df = pd.DataFrame(product_popularity.fetchall(), columns=['product_id', 'popularity'])

            # Step 6: Merge recommendations with popularity
            recommendations = recommendations.reset_index()
            recommendations.columns = ['product_id', 'co_purchase_score']
            recommendations = recommendations.merge(popularity_df, on='product_id')

            # Step 7: Sort by co-purchase score and then by popularity
            recommendations = recommendations.sort_values(['co_purchase_score', 'popularity'], ascending=False)

            # Step 8: Select the top recommendation
            top_recommendation = recommendations.iloc[0]['product_id']

            # Step 9: Save the recommendation
            new_reco = RecoModel(user_id=user_id, product_id=top_recommendation)
            self._session.add(new_reco)
            await self._session.commit()

    async def get_for_user(self, user_id: UserId) -> RecoEntity | None:
        result = await self._session.execute(
            select(self.model).where(self.model.user_id == user_id)
        )
        reco_model = result.scalar_one_or_none()

        if reco_model:
            return self.mapper.model_to_entity(reco_model)
        return None
