from aiogram.types import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row, Start, Cancel
from aiogram_dialog.widgets.text import Const

from app.controller.handler.user import UserHandler, ScoreHandler
from app.controller.handler.user.MarketHandler import MarketHandler
from app.view.state.admin import AdminStateGroup
from app.view.state.user import (
    SupportStateGroup, MarketStateGroup,
)
from app.view.state.user import ProductStateGroup
from app.view.static import StaticLoader
from app.widgets import back

menu = Window(
    StaticLoader.media("logo.png", ContentType.PHOTO),
    StaticLoader.template("market"),
    Row(
        Start(Const("👕 Футболки"), id="shirt", state=ProductStateGroup.t_shirt),
        Start(Const("🙋 Толстовки"), id="sweatshirts", state=ProductStateGroup.sweatshirt),
    ),
    Row(
        Start(Const("🍺 Кружки"), id="beer_cups", state=ProductStateGroup.beer_cups),
        Start(Const("📚 Прочее"), id="other", state=ProductStateGroup.other),
    ),
    Start(Const("📆 История заказов"), id="order_history", state=MarketStateGroup.order_history),
    Row(
        Cancel(back, id="back"),
        Start(Const("🛠️ Администрирование"), id="menu", state=AdminStateGroup.menu, when=UserHandler.is_admin),
    ),
    Start(Const("🆘 Поддержка"), id="support", state=SupportStateGroup.menu),
    state=MarketStateGroup.menu,
    getter=ScoreHandler.profile_score,
)
