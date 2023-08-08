from aiogram_dialog import Dialog

from app import dp
from app.view.dialog.user.market.beer_cups import window


def beer_cups_dialog():
    dialog = Dialog(window.menu, window.select, window.submit)
    dp.include_router(dialog)
