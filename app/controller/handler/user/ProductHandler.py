from typing import List, Dict, Any

from aiogram.types import Message, CallbackQuery, Chat
from aiogram_dialog import DialogManager, ChatEvent
from aiogram_dialog.widgets.common import Whenable
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import ManagedCheckboxAdapter

from app.api.dto.base import ApiResponse, PageResponse
from app.api.dto.product import ProductResponse, SubmitRequest
from app.api.service import ProductService
from app.database import User
from app.view.state.user.ProductStateGroup import ProductStateGroup


class ProductHandler:
    @staticmethod
    async def list_products(
            event_chat: Chat, dialog_manager: DialogManager, **kwargs
    ) -> Dict[str, List[ProductResponse]]:
        user: User = User.get_or_none(User.chat_id == event_chat.id)
        products = await ProductService.list_products(user.id)
        return {"products": products.data.content}

    @staticmethod
    async def select(callback: CallbackQuery, _: Any, dialog_manager: DialogManager, item_id: str):
        user: User = User.get_or_none(User.chat_id == callback.message.chat.id)
        product = await ProductService.find_by_id(item_id, user.id)
        if product.status != 200:
            await callback.message.reply(product.message)
            await dialog_manager.switch_to(ProductStateGroup.menu)
        else:
            await dialog_manager.update({"select": product.as_json()})
            await dialog_manager.switch_to(ProductStateGroup.select)

    @staticmethod
    async def render(dialog_manager: DialogManager, **kwargs):
        select = dialog_manager.dialog_data["select"]
        return ProductResponse.parse(select["data"]).as_dict()

    @staticmethod
    async def submit(message: Message, _: MessageInput, dialog_manager: DialogManager):
        select = dialog_manager.dialog_data["select"]
        product = ProductResponse.parse(select["data"])
        request = ProductHandler.submit_request(message)
        response = await ProductService.submit(product.id, request)
        await message.reply(response.message)
        await dialog_manager.switch_to(ProductStateGroup.menu)

    @staticmethod
    def submit_request(message: Message):
        user: User = User.get_or_none(User.chat_id == message.chat.id)
        return SubmitRequest(
            userId=str(user.id),
        )
