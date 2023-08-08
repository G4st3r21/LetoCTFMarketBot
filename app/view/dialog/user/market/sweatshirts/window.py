from operator import attrgetter

from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, SwitchTo, ScrollingGroup, Select, Cancel, Checkbox
from aiogram_dialog.widgets.text import Const

from app.controller.handler.user import ProductHandler
from app.widgets import back
from app.view.state.user import ProductStateGroup
from app.view.static import StaticLoader

menu = Window(
    StaticLoader.template("product/sweatshirt/list"),
    ScrollingGroup(
        Select(
            StaticLoader.template("product/sweatshirt/preview"),
            item_id_getter=attrgetter("id"),
            items="sweatshirt",
            id="sweatshirt_select",
            on_click=ProductHandler.select,
        ),
        width=1,
        height=5,
        id="sweatshirt_group",
    ),
    Cancel(back, id="back"),
    getter=ProductHandler.list_products,
    state=ProductStateGroup.menu,
)

select = Window(
    StaticLoader.template("product/sweatshirt/sweatshirt"),
    Row(
        SwitchTo(back, id="back", state=ProductStateGroup.menu),
        SwitchTo(
            Const("💸 Покупка"), id="submit", state=ProductStateGroup.submit
        ),
    ),
    getter=ProductHandler.render,
    state=ProductStateGroup.select,
)

submit = Window(
    Const("💸 Покупка"),
    SwitchTo(back, id="back", state=ProductStateGroup.select),
    MessageInput(ProductHandler.submit),
    state=ProductStateGroup.submit,
)
