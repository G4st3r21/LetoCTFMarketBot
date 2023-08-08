from aiogram_dialog import Dialog

from app import dp
from app.view.dialog.user.market.t_shirts import window


def t_shirts_dialog():
    dialog = Dialog(window.menu, window.select, window.submit)
    dp.include_router(dialog)
