from aiohttp import ClientSession

from app.api.dto.base import ApiResponse, PageResponse, PageRequest
from app.api.dto.orders import OrderHistoryResponse
from app.api.route import OrderRoute


class OrderHistoryService:
    @staticmethod
    async def list_orders(user_id: str) -> ApiResponse[PageResponse[OrderHistoryResponse]]:
        async with ClientSession() as api:
            orders = OrderRoute.list_orders()
            params = PageRequest(size=1_000_000).as_json()
            params.update({"userId": user_id})
            async with api.get(orders) as response:
                return await PageResponse.parse(response, OrderHistoryResponse)

    # @staticmethod
    # async def find_by_id(challenge_id: str, user_id: str) -> ApiResponse[ChallengeResponse]:
    #     async with ClientSession() as api:
    #         route = ChallengeRoute.find_by_id(challenge_id)
    #         params = {"userId": user_id}
    #         async with api.get(route, params=params) as response:
    #             return await ApiResponse.parse(response, ChallengeResponse)
