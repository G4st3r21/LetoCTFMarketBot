from app.config import RouteConfig


class OrderRoute:
    route = RouteConfig.load()

    @staticmethod
    def list_orders() -> str:
        return OrderRoute.route.url + "/api/v1/order"

    # @staticmethod
    # def find_by_id(challenge_id: str) -> str:
    #     return OrderRoute.route.url + f"/challenge/{challenge_id}"
    #
    # @staticmethod
    # def submit(challenge_id: str) -> str:
    #     return OrderRoute.route.url + f"/challenge/{challenge_id}/submit"
