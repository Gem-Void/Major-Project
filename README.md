# Major-Project
Sortify AI 📂🤖  Sortify AI is an intelligent file organization system that automatically scans, classifies, and sorts documents into appropriate categories using Machine Learning and OCR. It monitors folders in real time and organizes files without manual intervention.

Features
📄 Automatic document classification using Machine Learning
📁 Smart file organization into category folders
👀 Real-time folder monitoring with Watchdog
🔍 PDF text extraction
📝 DOCX document reading
📃 TXT file support
🖼️ OCR-based image text extraction using Tesseract
💾 SQLite database for document tracking
🖥️ Simple PyQt6 desktop interface
⚡ Automatic processing of both existing and newly added files

Supported File Types

PDF (.pdf)
Word Documents (.docx)
Text Files (.txt)
Images (.jpg, .png)
Categories

Currently supports automatic classification into categories such as:

Finance
Education
Shopping
Personal
Legal

with the ability to expand and train custom categories.

Tech Stack
Python
Scikit-Learn
TF-IDF Vectorization
Logistic Regression
SQLite
PyQt6
Watchdog
PDFPlumber
Tesseract OCR
Pillow

How It Works

User selects a folder to monitor.
Sortify AI scans existing files.
Text is extracted from documents and images.
The trained ML model predicts the document category.
Files are automatically moved into category-specific folders.
Document metadata is stored in SQLite for tracking and future retrieval.
