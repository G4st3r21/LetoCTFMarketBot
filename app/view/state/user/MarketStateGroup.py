from aiogram.fsm.state import StatesGroup, State


class MarketStateGroup(StatesGroup):
    menu = State()
    select = State()
    t_shirt = State()
    sweatshirt = State()
    beer_cups = State()
    other = State()
    order_history = State()
