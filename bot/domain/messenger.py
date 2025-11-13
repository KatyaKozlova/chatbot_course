from abc import ABC, abstractmethod


class Messenger(ABC):
    @abstractmethod
    def send_message(self, chat_id: int, text: str, **param) -> dict: ...

    @abstractmethod
    def get_updates(self, offset: int) -> dict: ...

    @abstractmethod
    def answer_callback_query(self, callback_query_id: str, **param) -> dict: ...

    @abstractmethod
    def delete_message(self, chat_id: int, message_id: int) -> dict: ...
