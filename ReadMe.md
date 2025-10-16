# PyCon Africa Quarto Workshop

This repository contains demo materials for the PyCon Africa workshop on **Quarto**, showing how to use Python to create reproducible reports and documents.

---

## What is Quarto?

[**Quarto**](https://quarto.org/) is an open-source publishing system that lets you create documents, presentations, and websites using Markdown, code, and notebooks.
It supports **R**, **Python**, **Julia**, and **Observable JS**.

---

## Prerequisites

Before you begin, make sure you have:

- [Python 3.8+](https://www.python.org/downloads/)
- [VSCode](https://code.visualstudio.com/) with:
  - Python extension
  - Quarto extension
- [LaTeX](https://quarto.org/docs/output-formats/pdf-engine.html#installing-tinytex) (TinyTeX recommended for PDF output)

To confirm Quarto is installed:

```bash
quarto check
```

## 📦 Setup Instructions

1. **Clone the repo**
2. **Create and activate a virtual environment (recommended)**
```
python3 -m venv venv
```
Activate it (Mac/Linux)
```
source venv/bin/activate
```
On Windows (PowerShell)
```
venv\Scripts\Activate
```
3. **Install dependencies**
```
python3 -m pip install -r requirements.txt
```
4. **Install LaTeX for PDF Rendering**
Quarto uses LaTeX to render PDF files.
Please install LaTeX based on your operating system:
**macOS**


