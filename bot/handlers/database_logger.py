import bot.telegram_client
import json
import os
import sqlite3

from bot.database_client import persist_update
from bot.handler import Handler
from dotenv import load_dotenv

load_dotenv()


class DatabaseLogger(Handler):
    def can_handle(self, update: dict) -> bool:
        return True

    def handle(self, update: dict) -> bool:
        persist_update(update)
        return True