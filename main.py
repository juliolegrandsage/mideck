
import argparse
import importlib.util
import mido
import rtmidi
import json
import threading


def load_func(path):
    spec = importlib.util.spec_from_file_location("func", path)
    func = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(func)
    return func

parser = argparse.ArgumentParser(description='mideck')
parser.add_argument("func", help="Path to func.py")
parser.add_argument("config", help="Path to config.json")

args = parser.parse_args()
func = load_func(args.func)
with open(args.config,'r', encoding="utf-8") as config_file:
    cfg = json.load(config_file)

def print_connected_devices():
    if len(mido.get_input_names()) > 0:
        print("Detected devices")
        for port in mido.get_input_names():
            print(f"Input: {port}")
    else:
        print("ERROR : No device detected, please plug a MIDI controller.")
def detect_midi():
    if len(mido.get_input_names()) > 0:
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

                elif msg.type == 'control_change':
                    func.set_vol(msg.value)

print_connected_devices()
# Threading


try:
    detect_midi()
except KeyboardInterrupt:
    print("fermeture")