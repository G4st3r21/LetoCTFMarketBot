from typing import List, Dict

from aiogram.types import Chat
from aiogram_dialog import DialogManager

from app.api.dto.orders import OrderHistoryResponse
from app.api.service import OrderHistoryService
from app.database import User


class OrderHistoryHandler:
    @staticmethod
    async def list_orders(
            event_chat: Chat, dialog_manager: DialogManager, **kwargs
    ) -> Dict[str, List[OrderHistoryResponse]]:
        user: User = User.get_or_none(User.chat_id == event_chat.id)
        orders = await OrderHistoryService.list_orders(user.id)
        return {"orders": orders.data.content}

    # @staticmethod
    # async def select(callback: CallbackQuery, _: Any, dialog_manager: DialogManager, item_id: str):
    #     user: User = User.get_or_none(User.chat_id == callback.message.chat.id)
    #     orders = await OrderHistoryService.find_by_id(item_id, user.id)
    #     if challenge.status != 200:
    #         await callback.message.reply(challenge.message)
    #         await dialog_manager.switch_to(ChallengeStateGroup.menu)
    #     else:
    #         await dialog_manager.update({"select": challenge.as_json()})
    #         await dialog_manager.switch_to(ChallengeStateGroup.select)

    # @staticmethod
    # async def render(dialog_manager: DialogManager, **kwargs):
    #     select = dialog_manager.dialog_data["select"]
    #     return ChallengeResponse.parse(select["data"]).as_dict()
