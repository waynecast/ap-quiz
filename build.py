# Builds questions.json for the A&P practice app from every bank in banks/.
# To add a quiz: create banks/quizN.py (copy quiz2.py's layout) and banks/cards_qN.py, then add both below.
import json, re
from collections import Counter
from banks import quiz1, quiz2, quiz3, cards_q1, cards_q2, cards_q3

QUIZZES = [(quiz1.QUIZ, cards_q1.CARDS), (quiz2.QUIZ, cards_q2.CARDS), (quiz3.QUIZ, cards_q3.CARDS)]

def diagram_cards(key, topic, img, label):
    return [(topic, f"{label} #{n}", name, src, img, f"#{n}", hint)
            for n, (name, hint, src) in key.items()]

EXTRA = {"q3": diagram_cards(quiz3.SKULL, 12, "img/skull.jpg", "Skull handout")
             + diagram_cards(quiz3.SPINE, 19, "img/spine.jpg", "Spine handout")}

def unit(qz, s):
    m = re.match(r"(L\d+)", s)
    assert m and m.group(1) in qz["units"], (qz["id"], s)
    return m.group(1)

out = {"title": "A&P Practice", "quizzes": []}
for qz, cards in QUIZZES:
    c = Counter(q["topic"] for q in qz["questions"])
    for t in qz["topics"]:
        assert c[t] >= 5, (qz["id"], t, c[t])
    for q in qz["questions"]:
        q["u"] = unit(qz, q["s"])
    deck = []
    for t, f, b, s in cards:
        assert t in qz["topics"], (qz["id"], t, f)
        deck.append({"topic": t, "f": f, "b": b, "s": s, "u": unit(qz, s)})
    # Diagram cards: front shows the image + number; reversed, it shows the image + structure name.
    for t, f, name, s, img, num, hint in EXTRA.get(qz["id"], []):
        deck.append({"topic": t, "f": f, "b": name, "n": hint, "s": s, "u": unit(qz, s), "img": img,
                     "rf": f"Find the {name[0].lower() + name[1:]}", "rb": num})
    fronts = Counter(d["f"] for d in deck)
    assert all(v == 1 for v in fronts.values()), [k for k, v in fronts.items() if v > 1]
    ct = Counter(d["topic"] for d in deck)
    names = {}
    for t in qz["topics"]:
        names.setdefault(qz["topics"][t], 0)
        names[qz["topics"][t]] += ct[t]
    assert all(v >= 2 for v in names.values()), names
    qz["cards"] = deck
    out["quizzes"].append(qz)
    print(qz["id"], len(qz["questions"]), "questions,", len(deck), "cards")
json.dump(out, open("questions.json", "w"), ensure_ascii=False, indent=1)
