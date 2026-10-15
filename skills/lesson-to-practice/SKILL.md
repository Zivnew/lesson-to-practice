---
name: lesson-to-practice
description: Turn one lesson's slides (.pptx or .pdf) into a student practice sheet with graded exercises, a find-the-bug exercise and a separate answer key, written in the slides' language. Use this whenever a teacher or instructor wants practice, homework, exercises, a worksheet, drills or "something for the students to work on" based on a specific lesson, presentation or slide deck, even if they don't say "practice sheet". Works best for programming lessons but suits any subject taught with slides.
---

# Lesson to practice sheet

Turn one lesson's slides into a practice sheet students can do on their own after class, plus an answer key for the teacher.

The most common failure is an exercise that needs something the students haven't learned yet. A student who gets stuck on a concept from next week learns that practice is frustrating, not that they've mastered this week's material. Every step below serves that one goal: practise exactly what this lesson taught, building on what came before, and nothing beyond it.

## Inputs

- **The lesson file** (.pptx or .pdf). Ask for it if the user didn't give one.
- **Where to save** (optional). By default, write a Markdown file named `practice-<lesson-name>.md` in a `notes/` folder next to the user's project. If no such folder fits, ask.
- **Number of exercises** (optional). Default: 6. Keep it between 5 and 8.

Treat the slides as read-only. Never move, rename or edit the original.

## Step 1: Read the slides

- **.pptx:** if `python-pptx` is installed, use it. Otherwise, run `scripts/pptx_text.py` from this skill's folder, which needs only Python's standard library:
  `python <this-skill-folder>/scripts/pptx_text.py "<lesson.pptx>" "<scratch>/lesson.txt"`
  Then read the output file. The script writes UTF-8, so Hebrew, Arabic and other non-Latin text survives. Printing straight to a Windows console can garble it.
- **.pdf:** use `pdftotext -layout`, or the pdf skill. For PDFs over 10 pages, check that poppler is installed first.

## Step 2: Map what the lesson taught

Before you write a single exercise, write yourself a short map (it doesn't go in the output):

1. **Taught in this lesson:** each concept, rule or convention, with a slide number. Include the "do and don't" rules, since they make great exercises.
2. **Assumed from before:** earlier topics the slides list (agenda or course-map slides often show the whole course), or use without explaining.
3. **Explicitly not yet:** anything the slides postpone ("next lesson we'll see…", "for now just write X"). Exercises must not need these. This is the list most often ignored, so check every exercise against it.
4. **Language and style:** the slides' language, and for code, the exact conventions they use: naming style, comment and documentation format, declaration order, and how input and output are done. Students copy what they see, so the sheet should look like the slides.

## Step 3: Write the exercises

Write the exercises easy to hard, so each one builds a little on the one before:

| Level | What it asks | Example kinds |
|---|---|---|
| Warm-up (1–2) | Recognise or read | "What does this print?", "Which signature is valid?", match the term to its meaning |
| Practice (2–3) | Apply one concept at a time | Write a small function or piece from a clear spec |
| Stretch (1–2) | Combine this lesson with earlier ones | A short task that uses this lesson's concept together with a loop, a condition, input, and so on |

For each exercise:
- Give a clear task, and for code, an example run (input → expected output) so students can check themselves.
- Use fresh scenarios. Don't copy the slides' worked examples or in-class exercises. Same skills, new context.
- Keep numbers small and outputs short enough to trace by hand.

**One "find the bug" exercise.** Give a short piece of code (or for non-code subjects, a short worked answer) with one or two mistakes taken from this lesson's warnings and "don't" slides. Ask students to find each mistake, explain it, and fix it. This is where the lesson's common-error slides pay off.

## Step 4: The answer key

Put it after a clear divider, under its own heading, so the teacher can cut it off before handing out the sheet. For each exercise:
- the solution, written in the slides' own conventions,
- one or two lines on *why*, pointing back to the concept (and slide number) it practises,
- for find-the-bug: each bug, why it's wrong, and the fixed version.

Before writing the key, trace every code answer by hand. A wrong answer key does more harm than no key.

## Output format

Write the sheet in the slides' language. Code, keywords and identifiers stay in their own language (usually English). For right-to-left languages, start each line with its words, not code, and put code in fenced blocks so it stays left-to-right.

```
# <Lesson title>: practice sheet

<One sentence: what this sheet practises.>

## Exercise 1 (warm-up): <short title>
...

## Exercise N (find the bug): <short title>
...

---

# Answer key (for the teacher)

## Exercise 1
...
```

Use the heading words in the sheet's language (for example, Hebrew instead of "Exercise" and "Answer key").

## Before you finish

Check each item, then tell the user where the file is and give a two-line summary of what it covers:
- [ ] Every exercise uses only what's in "taught" plus "assumed", and nothing from "not yet".
- [ ] There are 5–8 exercises, easy to hard, with exactly one find-the-bug.
- [ ] The answer key is complete, and every code answer was traced by hand.
- [ ] The conventions match the slides.
- [ ] There are no real names of students, teachers or schools in the sheet. Use generic placeholders if a name is needed.
