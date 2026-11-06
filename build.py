# Builds questions.json for the A&P practice app from every bank in banks/.
# To add a quiz: create banks/quizN.py (copy quiz2.py's layout) and add it to QUIZZES below.
import json, re
from collections import Counter
from banks import quiz1, quiz2, quiz3

QUIZZES = [quiz1.QUIZ, quiz2.QUIZ, quiz3.QUIZ]

out = {"title": "A&P Practice", "quizzes": []}
for qz in QUIZZES:
    c = Counter(q["topic"] for q in qz["questions"])
    for t in qz["topics"]:
        assert c[t] >= 5, (qz["id"], t, c[t])
    for q in qz["questions"]:
        m = re.match(r"(L\d+)", q["s"])
        assert m and m.group(1) in qz["units"], (qz["id"], q["s"])
        q["u"] = m.group(1)
    out["quizzes"].append(qz)
    print(qz["id"], len(qz["questions"]), "questions;", dict(sorted(c.items())))
json.dump(out, open("questions.json", "w"), ensure_ascii=False, indent=1)
