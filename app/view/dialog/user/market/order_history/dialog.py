from aiogram_dialog import Dialog

from app import dp
from app.view.dialog.user.market.order_history import window


def order_history_dialog():
    dialog = Dialog(window.order_history)
    dp.include_router(dialog)
