from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from ai.renamer import generate_filename

import time
import os

from organizer.file_mover import move_file
from organizer.file_renamer import rename_file

from extractor.pdf_reader import read_pdf
from extractor.docx_reader import read_docx
from extractor.text_reader import read_text
from extractor.image_reader import read_image

from ai.classifier import classify
from database.db import insert_document


class FileHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        file = event.src_path

        print("\n===================================")
        print("     REAL-TIME MONITORING")
        print("===================================\n")
        print("[NEW FILE DETECTED]")
        print("File :", os.path.basename(file))

        time.sleep(1)

        ext = os.path.splitext(file)[1].lower()

        text = ""

        print("\n[PROCESSING STARTED]")
        print("Extracting Text...")

        try:

            if ext == ".pdf":
                text = read_pdf(file)

            elif ext == ".docx":
                text = read_docx(file)

            elif ext == ".txt":
                text = read_text(file)

            elif ext in [".jpg", ".png"]:
                text = read_image(file)

            else:
                return

            label, confidence = classify(text)

            print("\n[CLASSIFICATION RESULT]")
            print("Predicted Category :", label)
            print("Confidence Score :", round(confidence * 100, 2), "%")

            new_name = generate_filename(text, label)

            print("\n[SMART FILE RENAMING]")
            print("Generated Name :", new_name)

            moved_path = move_file(file, label)

            final_path = rename_file(moved_path, new_name)

            print("\n[SMART FILE RENAMING]")
            print("Generated Name :", new_name)

            insert_document(
                os.path.basename(final_path),
                final_path,
                text,
                label,
                confidence
            )

            print("\n===================================")
            print("       FILE PROCESSED SUCCESSFULLY")
            print("===================================\n")

            print("File :", os.path.basename(final_path))
            print("Category :", label)

            print("\nStatus : SUCCESS")

            print("\n===================================\n")

        except Exception as e:

            print(f"[ERROR] {os.path.basename(file)} : {e}")


def scan_existing_files(folder):

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        # skip category folders
        if os.path.isdir(path):
            continue

        # skip db files
        if path.endswith(".db"):
            continue

        if not os.path.exists(path):
            continue

        ext = os.path.splitext(path)[1].lower()

        text = ""

        try:

            if ext == ".pdf":
                text = read_pdf(path)

            elif ext == ".docx":
                text = read_docx(path)

            elif ext == ".txt":
                text = read_text(path)

            elif ext in [".jpg", ".png"]:
                text = read_image(path)

            else:
                continue

            label, confidence = classify(text)

            new_name = generate_filename(text, label)

            moved_path = move_file(path, label)

            final_path = rename_file(moved_path, new_name)

            insert_document(
                os.path.basename(final_path),
                final_path,
                text,
                label,
                confidence
            )

            print(f"[SORTED] {os.path.basename(final_path)} → {label}")

        except Exception as e:

            print(f"[ERROR] {os.path.basename(path)} : {e}")


def start_watching(folder):

    print("\n===================================")
    print("      EXISTING FILE SCAN")
    print("===================================\n")

    print("Scanning existing files...")

    scan_existing_files(folder)

    event_handler = FileHandler()

    observer = Observer()

    observer.schedule(
        event_handler,
        folder,
        recursive=False
    )

    observer.start()

    print("\n===================================")
    print("      FOLDER MONITORING ACTIVE")
    print("===================================\n")

    print("Watching Folder :", folder)

    print("\nWaiting for new files...\n")

    print("Watching folder:", folder)

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()