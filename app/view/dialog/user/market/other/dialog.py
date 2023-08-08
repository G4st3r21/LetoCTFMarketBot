from aiogram_dialog import Dialog

from app import dp
from app.view.dialog.user.market.other import window


def other_dialog():
    dialog = Dialog(window.menu, window.select, window.submit)
    dp.include_router(dialog)
