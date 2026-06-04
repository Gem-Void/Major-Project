# Sortify AI 🤖📂

Sortify AI is an intelligent file organization system that automatically scans, classifies, and sorts documents into appropriate categories using Machine Learning and OCR.

## 🎯 Objectives

1. To develop a background monitoring service that detects new file events in real-time without user action.

2. To implement Tesseract OCR and Natural Language Processing (NLP) locally to extract semantic meaning from diverse file formats.

3. To develop an AI-driven classification engine that automatically Understand files meaningfully and moves them to a logical directory structure.

## ✨ Features

- Automatic document classification using Machine Learning
- Smart file organization into category folders
- Real-time folder monitoring with Watchdog
- PDF text extraction
- DOCX document reading
- TXT file support
- OCR-based image text extraction using Tesseract
- SQLite database for document tracking
- PyQt6 desktop interface

## 📄 Supported File Types

- PDF (.pdf)
- DOCX (.docx)
- TXT (.txt)
- JPG (.jpg)
- PNG (.png)

## 🏷 Categories

- Finance
- Education
- Shopping
- Personal
- Legal

## 🛠 Tech Stack

- Python
- Scikit-Learn
- TF-IDF
- Logistic Regression
- SQLite
- PyQt6
- Watchdog
- PDFPlumber
- Tesseract OCR
- Pillow

## ⚙️ How It Works

1. User selects a folder.
2. Sortify scans existing files.
3. Text is extracted from documents.
4. Machine Learning model predicts category.
5. File is moved into the appropriate folder.
6. Metadata is stored in SQLite.

## 🚀 Future Improvements

- Deep Learning classification
- Semantic search
- Duplicate detection
- Cloud integration
- Auto-renaming of files

## 👨‍💻 Author

Aditya Kaushik
