# lesson-to-practice

A Claude Code skill for teachers. You give it one lesson's slides (.pptx or .pdf), and it writes a practice sheet students can do after class:

- 5–8 exercises, from easy to hard, using only what the lesson taught plus earlier material, never topics the slides save for later
- one "find the bug" exercise, built from the lesson's own warnings and common mistakes
- an answer key after a divider, with explanations that point back to slide numbers, so you can cut it off before handing out the sheet
- written in the slides' language (it works well with Hebrew and other right-to-left languages), using the same coding conventions as the slides

It works best for programming lessons, but suits any subject taught with slides.

## Install

In Claude Code, run:

```
/plugin marketplace add Zivnew/lesson-to-practice
/plugin install lesson-to-practice@zivnew-skills
```

## Use

Ask in your own words, for example:

> Make a practice sheet for the students from `slides/lesson-05.pptx`

Or run the skill directly:

```
/lesson-to-practice:lesson-to-practice
```

By default the sheet is saved as `practice-<lesson-name>.md` in a `notes/` folder. Your slides are only read, never changed.

## Requirements

- Python 3, for reading .pptx files. The bundled script uses only Python's standard library.
- For .pdf slides: `pdftotext` (part of poppler).
