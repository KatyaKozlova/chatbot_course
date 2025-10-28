import bot.telegram_client
import json
import os
import sqlite3

from bot.database_client import persist_update
from bot.handlers.handler import Handler, HandlerStatus
from dotenv import load_dotenv

load_dotenv()


class DatabaseLogger(Handler):
    def can_handle(self, update: dict, state: str, order_json: dict) -> bool:
        return True

    def handle(self, update: dict, state: str, order_json: dict) -> bool:
        persist_update(update)
        return HandlerStatus.CONTINUE