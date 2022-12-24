# This Python file uses the following encoding: utf-8
import os
import sys
from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

BASE_DIR = os.path.dirname(__file__)


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('My App')
        label = QLabel()
        label.setPixmap(QPixmap(os.path.join(BASE_DIR, "cat.jpg")).scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio))
        label.setScaledContents(True)
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


if __name__ == "__main__":
    print("Current working folder:", os.getcwd())
    print("Paths are relative to:", BASE_DIR)
    app = QApplication([])
    window = Widget()
    window.show()
    sys.exit(app.exec())
