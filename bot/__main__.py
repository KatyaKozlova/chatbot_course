from bot.dispatcher import Dispatcher
from bot import get_handlers
from bot.long_polling import start_long_polling
from bot.infrastructure.messenger_telegram import MessengerTelegram
from bot.infrastructure.storage_sqlite import StorageSqlite


def main() -> None:
    try:
        StorageSqlite()
        MessengerTelegram()
        dispatcher = Dispatcher()
        dispatcher.add_handler(*get_handlers())
        start_long_polling(dispatcher)
    except KeyboardInterrupt:
        print("\nBye!")


if __name__ == "__main__":
    main()
