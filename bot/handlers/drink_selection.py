import json

import bot.telegram_client
import bot.database_client
from bot.handlers.handler import Handler, HandlerStatus

class DrinkSelectionHandler(Handler):
    def can_handle(self, update: dict, state: str, order_json: dict) -> bool:
        if "callback_query" not in update:
            return False
        
        if state!= "WAIT_FOR_PIZZA_SIZE":
            return False
        
        callback_data = update["callback_query"]["data"]
        return callback_data.startswith("size_")
    
    def handle(self, update: dict, state: str, order_json: dict) -> HandlerStatus:
        telegram_id=update["callback_query"]["from"]["id"]
        callback_data = update["callback_query"]["data"]

        pizza_size = callback_data.replace("size_", "").replace("_", " ").title()
        order_json["pizza_size"]=pizza_size
        bot.database_client.update_user_state_and_order(telegram_id, order_json)
        bot.database_client.update_user_state(telegram_id, "WAIT_FOR_DRINK")
        bot.telegram_client.answer_callback_query(update["callback_query"]["id"])
        bot.telegram_client.delete_message(
            chat_id=update["callback_query"]["message"]["chat"]["id"],
            message_id=update["callback_query"]["message"]["message_id"],
        )
        bot.telegram_client.send_message(
            chat_id=update["callback_query"]["message"]["chat"]["id"],
            text="Please select Drink",
            reply_markup=json.dumps(
                {
                    "inline_keyboard": [
                        [
                            {"text": "Water", "callback_data": "drink_cola"},
                            {"text": "Tea", "callback_data": "drink_juice"},
                        ],
                        [
                            {"text": "Cola", "callback_data": "drink_water"},
                            {"text": "Juice", "callback_data": "drink_tea"},
                        ],
                    ],
                },
            ),
        )
        return HandlerStatus.STOP