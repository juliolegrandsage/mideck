
import mido
import rtmidi
import func
import json
import lupa


lua = lupa.LuaRuntime()

def load_json():
    with open("config.json", "r") as config_file:
        return json.load(config_file)

cfg = load_json()

def print_connected_devices():
    print("Detected devices")
    for port in mido.get_input_names():
        print(f"Input: {port}") 

def detect_midi_note():
    with mido.open_input() as inport:
        for msg in inport:
            if msg.type == 'note_on' and msg.velocity > 0:
                print(f"Note On: {msg.note} Velocity: {msg.velocity}")

                action_name = cfg["mappings"].get(str(msg.note))
                if action_name:
                    action = getattr(func, action_name, None)
                    if action:
                        action()
                    else:
                        print(f"action '{action_name}' was not found")
            elif msg.type == 'note_off':
                print(f"Note Off: {msg.note} Velocity: {msg.velocity}")




print_connected_devices()

detect_midi_note()