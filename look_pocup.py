import json

with open("look.json") as f:
  l = json.load(f)
look = {k:{"9":v["9"]} for k, v in l.items()}

with open("./picup.json", mode="w") as f:
    json.dump(look,f)