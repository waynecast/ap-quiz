# A&P Practice

Mobile-friendly practice quizzes for NYIM A&P.

**Use it:** https://waynecast.github.io/ap-quiz/
Direct links: [Quiz #2](https://waynecast.github.io/ap-quiz/#q2) · [Quiz #1](https://waynecast.github.io/ap-quiz/#q1) · [Cumulative (midterm/final)](https://waynecast.github.io/ap-quiz/#exam)

| Quiz | Lectures | Subjects |
|---|---|---|
| Quiz #1 | 1–3 | Intro to A&P, Atoms & Molecules, Biochemistry & Cells |
| Quiz #2 | 4–6 | Cells, Tissues, Skin & Body Membranes |

- **Practice quiz:** one question per study-guide topic, in order. A new random set every time, with shuffled answer choices.
- **Practice by subject:** 20 random questions from one lecture (e.g. just Tissues).
- **Drill one topic:** every question for a single study-guide topic.
- **Cumulative exam practice:** for the midterm and final. Full (one question per topic from every quiz) or a 25-question quick mix.
- **Review missed:** retry the questions you got wrong, per quiz or across all quizzes. Progress is stored only in your own browser.
- Each answer shows a short explanation and the lecture/slide it comes from.
- Add it to your phone's home screen to open it like an app. It also works offline after the first visit.

## Editing questions

Each quiz has its own bank in `banks/` (`quiz1.py`, `quiz2.py`). Each question is one `add(...)` call:

```python
add(TOPIC_NUMBER, "Question?", "Correct answer",
    ["Wrong 1", "Wrong 2", "Wrong 3"], "Explanation.", "L4, slide 3")
```

Run `python3 build.py` to regenerate `questions.json`, then commit and push. To add a new quiz, copy `banks/quiz2.py` to `banks/quiz3.py`, edit it, and add it to `QUIZZES` in `build.py`; the cumulative exam picks it up automatically.

Generated questions (in `index.html`): Quiz #1 topics 4 (atomic mass/number) and 21 (pH); Quiz #2 topic 5 (DNA/RNA base pairing with random sequences).

Unofficial study aid made by a student. Not affiliated with or reviewed by NYIM.
