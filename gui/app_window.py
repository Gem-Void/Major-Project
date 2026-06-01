import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

import threading
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QVBoxLayout

from scanner.watcher import start_watching

class SortifyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sortify AI")
        self.setGeometry(200,200,400,200)

        layout = QVBoxLayout()

        self.label = QLabel("Select folder to monitor")

        self.button = QPushButton("Select Folder")
        self.button.clicked.connect(self.select_folder)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)


    def select_folder(self):

        folder = QFileDialog.getExistingDirectory(self,"Select Folder")

        if folder:

            self.label.setText(f"Monitoring: {folder}")

            watcher_thread = threading.Thread(
                target=start_watching,
                args=(folder,),
                daemon=True
            )

            watcher_thread.start()


app = QApplication(sys.argv)

window = SortifyApp()
window.show()

sys.exit(app.exec())