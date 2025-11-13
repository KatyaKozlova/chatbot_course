from bot.handlers.handler import Handler
from bot.handlers.database_logger import DatabaseLogger
from bot.handlers.ensure_user_exists import EnsureUserExists
from bot.handlers.message_start import MessageStart
from bot.handlers.pizza_size_selection import PizzaSelectionHandler
from bot.handlers.drink_selection import DrinkSelectionHandler
from bot.handlers.order_approval import ApprovalHandler
from bot.handlers.order_final_state import OrderFinalStateHandler


def get_handlers() -> list[Handler]:
    return [
        DatabaseLogger(),
        EnsureUserExists(),
        MessageStart(),
        PizzaSelectionHandler(),
        DrinkSelectionHandler(),
        ApprovalHandler(),
        OrderFinalStateHandler(),
    ]
