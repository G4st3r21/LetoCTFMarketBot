from aiogram.types import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row, Start, Cancel
from aiogram_dialog.widgets.text import Const

from app.controller.handler.user import UserHandler
from app.controller.handler.user.MarketHandler import MarketHandler
from app.view.state.admin import AdminStateGroup
from app.view.state.user import (
    ChallengeStateGroup,
    TeamStateGroup,
    ScoreStateGroup,
    EventStateGroup,
    SupportStateGroup,
)
from app.view.state.user.MarketStateGroup import MarketStateGroup
from app.view.static import StaticLoader
from app.widgets import back

menu = Window(
    StaticLoader.media("logo.png", ContentType.PHOTO),
    StaticLoader.template("profile"),
    Row(
        Start(Const("👕 Футболки"), id="shirt", state=MarketStateGroup.menu),
        Start(Const("🙋 Толстовки"), id="sweatshirts", state=MarketStateGroup.menu),
    ),
    Row(
        Start(Const("🍺 Кружки"), id="beer_cups", state=MarketStateGroup.user_scoreboard),
        Start(Const("📚 Прочее"), id="other", state=MarketStateGroup.team_scoreboard),
    ),
    Start(Const("📆 История заказов"), id="order_history", state=ScoreStateGroup.team_scoreboard),
    Row(
        Cancel(back, id="back"),
        Start(Const("🛠️ Администрирование"), id="menu", state=AdminStateGroup.menu, when=UserHandler.is_admin),
    ),
    Start(Const("🆘 Поддержка"), id="support", state=SupportStateGroup.menu),
    state=MarketStateGroup.menu,
    getter=MarketHandler.category_menu,
)
