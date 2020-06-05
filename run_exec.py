import time
from tqdm import tqdm
import vrcpy
import json
import itertools
from plyer import notification

interval = 30 * 60

while (True):
    with open("./setting.json", "r") as f:
        setting = json.load(f)

    client = vrcpy.Client()
    client.login(**setting)

    # main function
    with open("id_list.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = [l.split("#")[0] for l in lines]
    lines = [l.strip() for l in lines]
    lines = [l for l in lines if len(l) > 0]

    res = [client.fetch_user_by_id(l) for l in lines]
    res = [r for r in res if hasattr(r, "state")]

    online_friends = [r.displayName for r in res if r.state == "online"]

    if (len(online_friends) > 0):
        s = ", ".join(online_friends)
        notification.notify(
            title = "フレンドがオンラインです",
            message=f'{s} is online now',
            app_name='VRC Online Friend Checker',
        )

    for i in tqdm(range(interval)):
        time.sleep(1)
