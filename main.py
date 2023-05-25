from iot.devices import HueLight, SmartSpeaker, Curtains
from iot.message import MessageType, Message
from iot.service import IOTService


def main():
    # Create an instance of IOTService
    iot_service = IOTService()

    # Create instances of available devices
    hue_light = HueLight("hue_light_1")
    smart_speaker = SmartSpeaker("smart_speaker_1")
    curtains = Curtains("curtains")

    # Register devices
    hue_light_id = iot_service.register_device(hue_light)
    smart_speaker_id = iot_service.register_device(smart_speaker)
    curtains_id = iot_service.register_device(curtains)

    # Test devices
    iot_service.test_devices()

    message_wake_up_hue_light = Message(hue_light_id, MessageType.SWITCH_ON, "version")
    message_wake_up_smart_speaker = Message(smart_speaker_id, MessageType.PLAY_SONG, "version")
    message_wake_up_curtains = Message(curtains_id, MessageType.OPEN, "version")
    message_sleep_hue_light = Message(hue_light_id, MessageType.SWITCH_OFF, "version")
    message_sleep_smart_speaker = Message(smart_speaker_id, MessageType.SWITCH_OFF, "version")
    message_sleep_curtains = Message(curtains_id, MessageType.CLOSE, "version")


    # Create programs (lists of Message)
    program_wake_up = [message_wake_up_hue_light, message_wake_up_smart_speaker, message_wake_up_curtains]

    program_sleep = [message_sleep_hue_light, message_sleep_smart_speaker, message_sleep_curtains]

    # Run programs
    iot_service.run_program(program_wake_up)
    iot_service.run_program(program_sleep)

    # Unregister devices
    iot_service.unregister_device(hue_light_id)
    iot_service.unregister_device(smart_speaker_id)
    iot_service.unregister_device(curtains_id)

    # End program
    print("Program finished.")


if __name__ == "__main__":
    main()
