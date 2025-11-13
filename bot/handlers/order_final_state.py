import json

from bot.domain.messenger import Messenger
from bot.domain.storage import Storage
from bot.handlers.handler import Handler, HandlerStatus


class OrderFinalStateHandler(Handler):
    def can_handle(
        self,
        update: dict,
        state: str,
        order_json: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> bool:
        if "callback_query" not in update:
            return False

        if state != "WAIT_FOR_APPROVAL":
            return False

        callback_data = update["callback_query"]["data"]
        return callback_data.startswith("approval_")

    def handle(
        self,
        update: dict,
        state: str,
        order_json: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> HandlerStatus:
        telegram_id = update["callback_query"]["from"]["id"]
        callback_data = update["callback_query"]["data"]

        approval_answer = (
            callback_data.replace("approval_", "").replace("_", " ").title()
        )
        if approval_answer == "Yes":
            storage.update_user_state(telegram_id, "ORDER_FINISHED")
            messenger.delete_message(
                chat_id=update["callback_query"]["message"]["chat"]["id"],
                message_id=update["callback_query"]["message"]["message_id"],
            )
            messenger.send_message(
                chat_id=update["callback_query"]["message"]["chat"]["id"],
                text="Thank you for your order! Please wait! Your order is being prepared.",
            )
        elif approval_answer == "No":
            messenger.delete_message(
                chat_id=update["callback_query"]["message"]["chat"]["id"],
                message_id=update["callback_query"]["message"]["message_id"],
            )
            storage.clear_user_state_and_order(telegram_id)
            storage.update_user_state(telegram_id, "WAIT_FOR_PIZZA_NAME")
            messenger.send_message(
                chat_id=update["callback_query"]["message"]["chat"]["id"],
                text="Please, choose Pizza Type",
                reply_markup=json.dumps(
                    {
                        "inline_keyboard": [
                            [
                                {
                                    "text": "Margherita",
                                    "callback_data": "pizza_margherita",
                                },
                                {
                                    "text": "Pepperoni",
                                    "callback_data": "pizza_pepperoni",
                                },
                            ],
                            [
                                {
                                    "text": "Quatro Stagioni",
                                    "callback_data": "pizza_stagioni",
                                },
                                {
                                    "text": "Capricciosa",
                                    "callback_data": "pizza_capricciosa",
                                },
                            ],
                        ],
                    },
                ),
            )
        return HandlerStatus.STOP
