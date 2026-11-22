# A&P Practice

Mobile-friendly practice quizzes for NYIM A&P.

**Use it:** https://waynecast.github.io/ap-quiz/
Direct links: [Midterm](https://waynecast.github.io/ap-quiz/#mid) · [Quiz #4](https://waynecast.github.io/ap-quiz/#q4) · [Quiz #3](https://waynecast.github.io/ap-quiz/#q3) · [Quiz #2](https://waynecast.github.io/ap-quiz/#q2) · [Quiz #1](https://waynecast.github.io/ap-quiz/#q1)

| Quiz | Lectures | Subjects |
|---|---|---|
| **Midterm** | 1–15 | 50-question practice midterm: 40 written questions across every lecture (extra weight on Muscle Tissue and Endocrine, which had no quiz), then 10 diagram questions on 2 of 4 diagrams (pelvis, scapula, tibia/fibula, humerus), a new pair each time |
| Quiz #1 | 1–3 | Intro to A&P, Atoms & Molecules, Biochemistry & Cells |
| Quiz #2 | 4–6 | Cells, Tissues, Skin & Body Membranes |
| Quiz #3 | 7–9 | Skeletal System, Skull, Spine (with handout diagram matching) |
| Quiz #4 | 10–12 | Upper Extremity, Lower Extremity, Joints (with humerus, femur, forearm, leg, hand, foot, scapula, pelvis and shoulder-girdle diagram matching) |

- **Practice quiz:** one question per study-guide topic, in order. A new random set every time, with shuffled answer choices.
- **Practice by subject:** 20 random questions from one lecture (e.g. just Tissues).
- **Drill one topic:** every question for a single study-guide topic.
- **Flashcards:** every quiz has a deck (all cards, by lecture, or by topic). Tap to flip, then Got it or Again; "Again" cards come back at the end. Shuffle, reverse, and "only cards I haven't gotten yet" options. The skull and spine cards show the handout diagram.
- **Review missed:** retry the questions you got wrong in each quiz. Progress is stored only in your own browser.
- Each answer shows a short explanation and the lecture/slide it comes from.
- **Story mode** (`story.html`): narrated review stories. The picture, key terms and words appear on screen while it reads, and it keeps playing with the screen locked. First story: *Calcium's Journey* (Lectures 1–15).
- Add it to your phone's home screen to open it like an app. It also works offline after the first visit.

## Editing questions

Each quiz has its own bank in `banks/` (`quiz1.py` … `quiz4.py`). Diagram topics (Quiz #3 topics 12–25, Quiz #4 topics 11–25) are generated from the label keys in each bank and show the class handout image from `img/`. Quiz #4's keys match the completed class diagrams. Each question is one `add(...)` call:

```python
add(TOPIC_NUMBER, "Question?", "Correct answer",
    ["Wrong 1", "Wrong 2", "Wrong 3"], "Explanation.", "L4, slide 3")
```

Flashcards live in `banks/cards_qN.py`, one `(topic, front, back, source)` line per card. Quiz #3's skull and spine cards are generated from the label keys in `quiz3.py`.

Run `python3 build.py` to regenerate `questions.json`, then commit and push. To add a new quiz, create `banks/quizN.py` and `banks/cards_qN.py` (copy an existing one), then add both to `QUIZZES` in `build.py`.

The midterm bank is `banks/midterm.py`. It reuses questions from the quiz banks by topic and adds new ones for compact bone, glands, hormones (matching the class Hormones chart) and muscle. Diagram questions carry a `dg` tag; the app picks 2 diagrams per exam (`dgTopics` / `dgNames` in the bank).

The older cumulative exam mode is built in but switched off. Set `EXAM_MODE = true` in `index.html` to turn it on before an exam.

Generated questions (in `index.html`): Quiz #1 topics 4 (atomic mass/number) and 21 (pH); Quiz #2 topic 5 (DNA/RNA base pairing with random sequences).

Unofficial study aid made by a student. Not affiliated with or reviewed by NYIM.

## Story mode

Each story is a Python script in `stories/src/` (scenes with a lecture tag, title, image, key terms and short lines). `stories/src/build_story.py` narrates every line with the Kokoro neural voice (`kokoro-onnx`), joins them into one MP3 and writes the JSON cue sheet the player uses to sync the captions. Images live in `img/story/`. List each story in `stories/index.json`.
