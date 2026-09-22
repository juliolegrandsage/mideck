import subprocess
import webbrowser
import os
import obsws_python as obs

# You can add your own commands in this file by creating a function and giving it a midi note in "config.json"


def open_youtube():
    webbrowser.open("https://www.youtube.com/")

def open_steam():
    subprocess.Popen(r"C:\Program Files (x86)\Steam\steam.exe")

def launch_cs():
    subprocess.Popen(r"C:\Program Files (x86)\Steam\steam.exe")
    subprocess.Popen(r"C:\Program Files (x86)\Steam\steam.exe -applaunch 730")

def mute_obs():
    client = obs.ReqClient(
        host="localhost",
        port=4455,
        password="jahrastafari"
    )
    client.toggle_input_mute("Mic/Aux")