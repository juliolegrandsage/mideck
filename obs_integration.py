from obswebsocket import obsws, requests

obs_client = obsws(
    "localhost",
    4455
)

obs_client.connect()


def change_obs_scene(name):
    obs_client.call(requests.SetCurrentProgramScene(sceneName = name))