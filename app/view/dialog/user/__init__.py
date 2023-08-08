from app.view.dialog.admin.menu.dialog import admin_dialog
from app.view.dialog.user.market.sweatshirts.dialog import sweatshirts_dialog
from app.view.dialog.user.market.other.dialog import other_dialog
from app.view.dialog.user.market.order_history.dialog import order_history_dialog
from app.view.dialog.user.market.t_shirts.dialog import t_shirts_dialog
from app.view.dialog.user.market.beer_cups.dialog import beer_cups_dialog
from app.view.dialog.user.challenge.dialog import challenge_dialog
from app.view.dialog.user.event.dialog import event_dialog
from app.view.dialog.user.score.dialog import score_dialog
from app.view.dialog.user.support.dialog import support_dialog
from app.view.dialog.user.team.dialog import team_dialog


def user_dialogs():
    team_dialog()
    challenge_dialog()
    score_dialog()
    event_dialog()
    admin_dialog()
    support_dialog()
    user_market_dialogs()


def user_market_dialogs():
    beer_cups_dialog()
    other_dialog()
    order_history_dialog()
    t_shirts_dialog()
    sweatshirts_dialog()
