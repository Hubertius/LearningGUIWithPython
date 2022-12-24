# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My App")

        checkBox = QCheckBox("This is a checkbox")
        checkBox.setCheckState(Qt.Checked)
        checkBox.stateChanged.connect(self.show_state)
        self.setCentralWidget(checkBox)

    def show_state(self, state):
        print(state == Qt.Checked)
        print(state)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
