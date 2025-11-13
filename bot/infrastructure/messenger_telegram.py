import json
import os
import urllib.request

from bot.domain.messenger import Messenger

from dotenv import load_dotenv

load_dotenv()


class MessengerTelegram(Messenger):
    def make_request(self, method: str, **param) -> dict:
        json_data = json.dumps(param).encode("utf-8")

        request = urllib.request.Request(
            method="POST",
            url=f"{os.getenv('TELEGRAM_BASE_URI')}/{method}",
            data=json_data,
            headers={"Content-Type": "application/json"},
        )

        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")
            response_json = json.loads(response_body)
            assert response_json["ok"]
            return response_json["result"]

    def get_updates(self, offset: int) -> dict:
        return self.make_request("getUpdates", offset=offset)

    def send_message(self, chat_id: int, text: str, **param) -> dict:
        return self.make_request("sendMessage", chat_id=chat_id, text=text, **param)

    def answer_callback_query(self, callback_query_id: str, **param) -> dict:
        return self.make_request(
            "answerCallbackQuery", callback_query_id=callback_query_id, **param
        )

    def delete_message(self, chat_id: int, message_id: int) -> dict:
        return self.make_request(
            "deleteMessage", chat_id=chat_id, message_id=message_id
        )
