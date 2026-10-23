# A&P Quiz #1 Practice

A mobile-friendly practice quiz for NYIM A&P Quiz #1 (Lectures 1–3).

**Use it:** https://waynecast.github.io/ap-quiz/

- **Practice quiz:** 25 questions, one per study-guide topic, in order (1 → 25). A new random set every time, with shuffled answer choices.
- **Drill one topic:** every question for a single topic.
- **Review missed:** retry the questions you got wrong. Progress is stored only in your own browser.
- Each answer shows a short explanation and the lecture/slide it comes from (L1 = Intro to A&P, L2 = Atoms & Molecules, L3 = Biochemistry & Cells).
- Add it to your phone's home screen to open it like an app. It also works offline after the first visit.

## Editing questions

Questions live in `build_bank.py`. Each one is a single `add(...)` call:

```python
add(TOPIC_NUMBER, "Question?", "Correct answer",
    ["Wrong 1", "Wrong 2", "Wrong 3"], "Explanation.", "L1, slide 3")
```

Run `python3 build_bank.py` to regenerate `questions.json`, then commit and push. Topics 4 (atomic mass/number) and 21 (pH) also get generated questions from the code in `index.html`.

Unofficial study aid made by a student. Not affiliated with or reviewed by NYIM.
