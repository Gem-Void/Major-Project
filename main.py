
import sys
import os

sys.path.append(os.getcwd())

from scanner.scanner import scan_folder

from extractor.pdf_reader import read_pdf
from extractor.docx_reader import read_docx
from extractor.text_reader import read_text
from extractor.image_reader import read_image

from ai.classifier import classify

from database.db import insert_document


folder = "files_to_scan"

files = scan_folder(folder)

print("Files found:", files)

for file in files:

    ext = os.path.splitext(file)[1]

    text = ""

    if ext == ".pdf":
        text = read_pdf(file)

    elif ext == ".docx":
        text = read_docx(file)

    elif ext == ".txt":
        text = read_text(file)

    elif ext in [".jpg",".png"]:
        text = read_image(file)

    label = classify(text)

    insert_document(os.path.basename(file), file, text, label)

    print(file,"→",label)