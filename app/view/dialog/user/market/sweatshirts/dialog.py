from aiogram_dialog import Dialog

from app import dp
from app.view.dialog.user.market.sweatshirts import window


def sweatshirts_dialog():
    dialog = Dialog(window.menu, window.select, window.submit)
    dp.include_router(dialog)
