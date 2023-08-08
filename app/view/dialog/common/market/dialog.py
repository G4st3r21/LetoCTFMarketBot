from aiogram_dialog import Dialog

from app import dp
from app.view.dialog.common.market import window


def market_menu_dialog():
    dialog = Dialog(window.menu)
    dp.include_router(dialog)
