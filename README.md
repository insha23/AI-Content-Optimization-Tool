# AI Content Optimization Tool (GEO)

A web-based application that analyzes and improves textual content for better readability, clarity, and performance in AI-driven search environments.

## Live Demo
https://ai-content-optimization-tool.streamlit.app/

---

## Overview

This project evaluates content quality using metrics such as readability, keyword usage, structural organization, and vocabulary diversity. It also provides suggestions to improve content so that it becomes easier to understand for both users and AI-based search systems.

---

## Features

- Readability analysis using Flesch Reading Ease and Grade Level
- Keyword frequency detection
- Content structure analysis through heading detection
- Lexical diversity measurement
- Automated content improvement suggestions
- Word cloud visualization
- Text simplification feature for converting complex text into easier text
- Downloadable analysis report

---

## Tech Stack

- Python
- Streamlit
- NLTK
- Textstat
- Matplotlib
- WordCloud

---

## How It Works

1. Enter or paste content into the input box
2. Provide a target keyword
3. Click **Analyze Content**
4. View results such as readability score, keyword usage, and suggestions
5. Optionally simplify the text using the built-in feature
6. Download the generated analysis report

---

## Installation and Setup

```bash
git clone https://github.com/insha23/AI-Content-Optimization-Tool.git
cd AI-Content-Optimization-Tool
pip install -r requirements.txt
streamlit run app.py
