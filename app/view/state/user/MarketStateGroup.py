from aiogram.fsm.state import StatesGroup, State


class MarketStateGroup(StatesGroup):
    menu = State()
    select = State()
    order_history = State()

