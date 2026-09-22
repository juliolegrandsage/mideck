import subprocess
import webbrowser
# import os


# You can add your own commands in this file by creating a function and giving it a midi note in "config.json"


def open_steam():
    subprocess.call(r"C:\Program Files (x86)\Steam\steam.exe")

def open_youtube():
    webbrowser.open("www.youtube.com/")