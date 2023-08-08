from aiohttp import ClientSession

from app.api.dto.base import ApiResponse, PageResponse, PageRequest
from app.api.dto.product import ProductResponse, SubmitRequest
from app.api.route import ProductRoute


class ProductService:
    @staticmethod
    async def list_products(user_id: str) -> ApiResponse[PageResponse[ProductResponse]]:
        async with ClientSession() as api:
            route = ProductRoute.list_product()
            params = PageRequest(size=1_000_000).as_json()
            params.update({"userId": user_id})
            async with api.get(route, params=params) as response:
                return await PageResponse.parse(response, ProductResponse)

    @staticmethod
    async def find_by_id(product_id: str, user_id: str) -> ApiResponse[ProductResponse]:
        async with ClientSession() as api:
            route = ProductRoute.find_by_id(product_id)
            params = {"userId": user_id}
            async with api.get(route, params=params) as response:
                return await ApiResponse.parse(response, ProductResponse)

    @staticmethod
    async def submit(product_id: str, request: SubmitRequest) -> ApiResponse:
        async with ClientSession() as api:
            route = ProductRoute.submit(product_id)
            async with api.post(route, json=request.as_json()) as response:
                return await ApiResponse.parse(response)
