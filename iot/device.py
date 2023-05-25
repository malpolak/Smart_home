from abc import ABC, abstractmethod
from iot.message import MessageType


class Device(ABC):
    def __init__(self, name):
        self.name = name
        self.id = None

    def set_id(self, device_id):
        self.id = device_id

    def get_id(self):
        return self.id

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def send_message(self, message_type: MessageType, data: str) -> None:
        pass

    @abstractmethod
    def status_update(self) -> str:
        pass
