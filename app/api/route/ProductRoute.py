import os

from app.config import RouteConfig


class ProductRoute:
    route = RouteConfig.load()

    @staticmethod
    def list_product() -> str:
        return os.getenv("API_URL2") + "/api/v1/product"

    @staticmethod
    def find_by_id(product_id: str) -> str:
        return os.getenv("API_URL2") + f"/api/v1/product/{product_id}"

    @staticmethod
    def submit(product_id: str) -> str:
        return os.getenv("API_URL2") + f"/api/v1/challenge/{product_id}/submit"
