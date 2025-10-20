import bot.database_client
import bot.telegram_client
import time
from bot.dispatcher import Dispatcher
from bot.handlers.database_logger import DatabaseLogger
from bot.handlers.message_echo import MessageEcho
from bot.handlers.message_photo_echo import MessagePhotoEcho
from bot.long_polling import start_long_polling

def main() -> None:
    next_update_offset=0
    try:
        dispatcher = Dispatcher()
        dispatcher.add_handler(DatabaseLogger(), MessagePhotoEcho(), MessageEcho())
        start_long_polling(dispatcher)
    except KeyboardInterrupt:
        print("\nBye!")
    

if __name__ == "__main__":
    main()