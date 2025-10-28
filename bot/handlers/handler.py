from abc import ABC, abstractmethod
from enum import Enum

class HandlerStatus(Enum):
    CONTINUE = 1
    STOP = 2

class Handler(ABC):
    @abstractmethod
    def can_handle(self, update: dict, state: str, order_json: dict) -> bool: ...

    def handle(self, update: dict, state: str, order_json: dict) -> HandlerStatus:
        """
        return options:
        - true - signal for dispatcher to continue processing
        - false - signal for dispatcher to STOP processing
        """
        pass