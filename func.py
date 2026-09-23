import subprocess
import webbrowser
from pycaw.pycaw import AudioUtilities
# import os


# You can add your own commands in this file by creating a function and giving it a midi note in "config.json"



# Parameters for volume control
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume


def open_steam():
    subprocess.call(r"C:\Program Files (x86)\Steam\steam.exe")

def open_youtube():
    webbrowser.open("www.youtube.com/")
    
def set_vol(value):

    
    value = value / 127    
    volume.SetMasterVolumeLevelScalar(value, None)
    