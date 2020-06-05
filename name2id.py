import vrcpy
import json
import itertools

with open("./setting.json", "r") as f:
    setting = json.load(f)

client = vrcpy.Client()
client.login(**setting)

with open("name_list.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
lines = [l.strip() for l in lines]

res = [client.api.call("/users", params={"search":name}) for name in lines]
res = list(itertools.chain.from_iterable([r["data"] for r in res]))
res = [{"id": r["id"], "username": r["username"], "displayName": r["displayName"]} for r in res]

s = [f'{r["id"]}: {r["displayName"]}/{r["username"]}' for r in res]
print("\n".join(s))

with open("id_list.txt", "w", encoding="utf-8") as f:
    for r in res:
        f.write(f'{r["id"]} # {r["displayName"]}/{r["username"]}\n')
