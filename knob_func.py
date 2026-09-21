from pycaw.pycaw import AudioUtilities, AudioDevice

# volume control utils
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume


def increase_volume(value):
    current_volume = volume.GetMasterVolumeLevelScalar()

    volume.SetMasterVolumeLevelScalar(value / 127, None)