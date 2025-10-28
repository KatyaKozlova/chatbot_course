import json

import bot.telegram_client
import bot.database_client
from bot.handlers.handler import Handler, HandlerStatus



class MessageStart(Handler):
    def can_handle(self, update: dict, state: str, data: dict) -> bool:
        return (
            "message" in update
            and "text" in update["message"]
            and update["message"]["text"] == "/start" 
        )

    def handle(self, update: dict, state: str, data: dict) -> HandlerStatus:
        telegram_id=update["message"]["from"]["id"]

        bot.database_client.clear_user_state_and_order(telegram_id)
        bot.database_client.update_user_state(telegram_id, "WAIT_FOR_PIZZA_NAME")

        bot.telegram_client.send_message(
            chat_id=update["message"]["chat"]["id"],
            text="Welcome to Pizza shop!",
            reply_markup=json.dumps({"remove_keyboard": True}),
        )

        bot.telegram_client.send_message(
            chat_id=update["message"]["chat"]["id"],
            text="Please, choose Pizza Type",
            reply_markup=json.dumps(
                {
                    "inline_keyboard": [
                        [
                            {"text": "Margherita", "callback_data": "pizza_margherita"},
                            {"text": "Pepperoni", "callback_data": "pizza_pepperoni"},
                        ],
                        [
                            {
                                "text": "Quatro Stagioni", 
                                "callback_data": "pizza_stagioni" ,  
                            },
                            {
                                "text": "Capricciosa", 
                                "callback_data": "pizza_capricciosa" ,  
                            },
                        ],
                    ],
                },
            ),
        )
        return HandlerStatus.STOP