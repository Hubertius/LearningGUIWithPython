# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from random import choice
'''
window_titles = [
"My App",
"My App",
"Still My App",
"Still My App",
"What on earth",
"What on earth",
"This is surprising",
"This is surprising",
"Something went wrong",
]

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.is_button_checked = True
        self.setWindowTitle("My App")
        self.button = QPushButton("Press me!")
        self.n_times_clicked = 0
        self.button.clicked.connect(self.the_button_was_toggled)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.setCentralWidget(self.button)
        self.setFixedSize(QSize(400,300))

    def the_button_was_toggled(self, checked):
        self.button.setText("You already clicked me")
        new_window_title = choice(window_titles)
        print('Setting title %s' % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print('Window title changed: %s' % window_title)
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)
'''

class MainWindow(QMainWindow):
    def __init__(self, paren=None):
        super().__init__()

        self.setWindowTitle("My App")
        self.label = QLabel()

        self.input = QLineEdit()
        self.buttonAccept = QPushButton()
        self.buttonClear = QPushButton()
        self.buttonAccept.clicked.connect(lambda: self.label.setText(self.input.text()))
        self.buttonClear.clicked.connect(lambda: self.label.setText(""))
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.buttonAccept)
        layout.addWidget(self.buttonClear)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
