from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel

from app.controller.handler.user import OrderHistoryHandler
from app.view.state.user import MarketStateGroup
from app.widgets import back
from app.view.static import StaticLoader

order_history = Window(
    StaticLoader.template("orders"),
    Cancel(back, id="back"),
    state=MarketStateGroup.order_history,
    getter=OrderHistoryHandler.list_orders,
)

# select = Window(
#     StaticLoader.template("product/product"),
#     Row(
#         SwitchTo(back, id="back", state=ProductStateGroup.menu),
#         SwitchTo(
#             Const("💸 Покупка"), id="submit", state=ProductStateGroup.submit
#         ),
#     ),
#     getter=OrderHistoryHandler.render,
#     state=ProductStateGroup.select,
# )

# submit = Window(
#     Const("💸 Покупка"),
#     SwitchTo(back, id="back", state=ProductStateGroup.select),
#     # MessageInput(OrderHistoryHandler.submit),
#     state=ProductStateGroup.submit,
# )
