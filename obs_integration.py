from obswebsocket import obsws, requests
import psutil

if "obs64.exe" in (p.name() for p in psutil.process_iter()):

    obs_client = obsws(
        "localhost",
        4455
    )

    obs_client.connect()

    def change_obs_scene(name):
        obs_client.call(requests.SetCurrentProgramScene(sceneName = name))
else:
    print("obs pas lancé")