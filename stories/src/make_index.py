"""Rebuild stories/index.json from every stories/*.json cue sheet."""
import json, glob, os
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
items = []
for f in glob.glob(os.path.join(root, "*.json")):
    if f.endswith("index.json"): continue
    d = json.load(open(f))
    items.append({k: d.get(k) for k in ("id", "group", "num", "title", "subtitle", "lectures", "duration")})
order = {"thread": 0, "lecture": 1}
items.sort(key=lambda d: (order.get(d["group"], 2), d.get("num") or 0, d["title"]))
json.dump(items, open(os.path.join(root, "index.json"), "w"), ensure_ascii=False, indent=1)
print(len(items), "stories")
