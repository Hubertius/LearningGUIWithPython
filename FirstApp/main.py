# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press me!")
        self.setCentralWidget(button)
        self.setFixedSize(QSize(400,300))


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
