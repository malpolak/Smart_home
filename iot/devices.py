from iot.device import Device

class HueLight(Device):
    def connect(self):
        print("Connecting Hue Light")

    def disconnect(self):
        print("Disconnecting Hue Light")

    def send_message(self, msg_type, data):
        print(f"Hue light handling message of type {msg_type.name} with data [{data}]")

    def status_update(self):
        print("hue_light_status_ok")


class SmartSpeaker(Device):
    def connect(self):
        print("Connecting Smart Speaker")

    def disconnect(self):
        print("Disconnecting Smart Speaker")

    def send_message(self, message_type, data):
        print(
            f"Smart Speaker handling message of type {message_type.name} with data [{data}]"
        )

    def status_update(self):
        print("smart_speaker_status_ok")


class Curtains(Device):
    def connect(self):
        print("Connecting Curtains")

    def disconnect(self):
        print("Disconnecting Curtains")

    def send_message(self, message_type, data):
        print(
            f"Curtains handling message of type {message_type.name} with data [{data}]"
        )

    def status_update(self):
        print("curtains_status_ok")
