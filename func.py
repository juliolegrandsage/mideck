import subprocess
import webbrowser
from pycaw.pycaw import AudioUtilities
import screen_brightness_control
import obsws_python
# import os

obs_client = obsws_python.ReqClient(host="localhost", port="4455")


# You can add your own commands in this file by creating a function and giving it a midi note in "config.json"



# Parameters for volume control
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume


def open_steam():
    subprocess.call(r"C:\Program Files (x86)\Steam\steam.exe")

def open_youtube():
    webbrowser.open("www.youtube.com/")
    
def mute():
    volume.SetMute(not volume.GetMute(), None)

def mute_obs():
    obs_client.toggle_input_mute('Mic/Aux')

def set_vol(value):

    
    value = value / 127    
    volume.SetMasterVolumeLevelScalar(value, None)
    print(volume.GetMasterVolumeLevelScalar())
    if volume.GetMasterVolumeLevelScalar() <= 0:
        volume.SetMute(1, None)
    else:
        volume.SetMute(0, None)
        

def set_brightness(value):
    
    screen_brightness_control.set_brightness(value)

