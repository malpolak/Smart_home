import string
import random
from iot.diagnostics import collect_diagnostics


class IOTService:
    def __init__(self):
        self.devices = []

    def generate_id(self, length=10):
        return "".join(random.choice(string.ascii_uppercase) for _ in range(length))

    def register_device(self, device):
        device.connect()
        device_id = self.generate_id()
        device.set_id(device_id)
        self.devices.append(device)
        return device_id

    def unregister_device(self, device_id):
        for device in self.devices:
            if device.get_id() == device_id:
                device.disconnect()
                self.devices.remove(device)
                break

    def get_device(self, device_id):
        for device in self.devices:
            if device.get_id() == device_id:
                return device
        return None

    def run_program(self, messages):
        print("=====RUNNING PROGRAM======")
        for message in messages:
            device_id = message.device_id
            device = self.get_device(device_id)
            if device:
                msg_type = message.msg_type
                data = message.data
                device.send_message(msg_type, data)
        print("=====END OF PROGRAM======")

    def test_devices(self):
        print("Start test devices")
        for device in self.devices:
            collect_diagnostics(device)
