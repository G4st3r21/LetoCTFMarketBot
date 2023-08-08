from aiogram.fsm.state import StatesGroup, State


class ProductStateGroup(StatesGroup):
    menu = State()
    select = State()
    submit = State()
    t_shirt = State()
    sweatshirt = State()
    beer_cups = State()
    other = State()
