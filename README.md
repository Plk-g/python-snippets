# 🐍 Python Snippets

A collection of practical Python techniques and library demos — covering web scraping, performance benchmarking, and more. Each file is self-contained and focused on a single concept.

---

## 📁 Contents

| File | Topic | Libraries |
|------|-------|-----------|
| [`scraping_demo.py`](./scraping_demo.py) | Web scraping with requests and BeautifulSoup | `requests`, `bs4`, `lxml` |
| [`timing_your_code.ipynb`](./timing_your_code.ipynb) | 3 ways to benchmark Python code performance | `time`, `timeit` |

---

## 🔍 File Breakdown

### `scraping_demo.py` — Web Scraping
Demonstrates how to fetch and parse HTML from websites using `requests` and `BeautifulSoup`. Covers:
- Making HTTP GET requests
- Parsing HTML with `lxml`
- Selecting elements by CSS class and tag
- Extracting text and attributes from parsed content

> ⚠️ Always check a website's `robots.txt` and terms of service before scraping. The examples here use publicly accessible pages or sites built for scraping practice.

---

### `timing_your_code.ipynb` — Performance Benchmarking
Explores three different approaches to measuring how long Python code takes to run:

1. **`time` module** — manual start/end timestamps for measuring elapsed wall time
2. **`timeit` module** — precise benchmarking by running a statement thousands of times
3. **`%%timeit` magic** — Jupyter-native cell-level benchmarking with mean and std deviation

Includes a concrete comparison between a list comprehension and `map()` approach to illustrate real performance differences.

---

## ⚙️ Setup

**Requirements:** Python 3.8+

Install dependencies:

```bash
pip install requests bs4 lxml
```

To run the notebook, use Jupyter or open it directly in VS Code:

```bash
jupyter notebook timing_your_code.ipynb
```

---

## 🚀 Running the Script

```bash
python scraping_demo.py
```

---

## 📌 Topics Covered

- HTTP requests and response handling
- HTML parsing and CSS selector targeting
- Code performance profiling and benchmarking
- List comprehensions vs. `map()` performance

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Libraries:** `requests`, `BeautifulSoup4`, `lxml`, `timeit`
- **Notebook:** Jupyter / IPython
