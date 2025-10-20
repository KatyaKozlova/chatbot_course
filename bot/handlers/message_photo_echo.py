from bot.handler import Handler
import bot.telegram_client

class MessagePhotoEcho(Handler):
    def can_handle(self, update: dict) -> bool:
        return "message" in update and "photo" in update["message"]

    def handle(self, update: dict) -> bool:
        photo_list = update["message"]["photo"]
        max_photo = max(photo_list, key=lambda p: p.get("file_size", 0))
        file_id = max_photo["file_id"]
        bot.telegram_client.sendPhoto(
            chat_id=update["message"]["chat"]["id"],
            photo=file_id,
        )
        return False