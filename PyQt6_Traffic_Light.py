```
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication
from PyQt6.QtCore import QTimer
import sys

class MainWIdget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(180, 500)

        self.layout = QVBoxLayout()
        self.buttonRed = QPushButton()
        self.buttonYellow = QPushButton()
        self.buttonGreen = QPushButton()

        self.layout.addWidget(self.buttonRed)
        self.layout.addWidget(self.buttonYellow)
        self.layout.addWidget(self.buttonGreen)
        self.setStyleSheet("background-color: black;")

        self.setLayout(self.layout)
        self.timer = QTimer(self)
        self.setRed()

    def setRed(self):
        self.buttonRed.setStyleSheet("background-color: red; border: 1px solid black; border-radius: 75px; width: 150px; height: 150px;")
        self.buttonYellow.setStyleSheet("background-color: black; border: 1px solid black; border-radius: 75px; width: 150px; height: 150px;")
        self.buttonGreen.setStyleSheet("background-color: black; border: 1px solid black; border-radius: 75px; width: 150px; height: 150px;")
        self.timer.singleShot(2000, self.setRedYellow)

    def setRedYellow(self):
        self.buttonYellow.setStyleSheet("background-color: yellow; border: 1px solid black; border-radius: 75px; width: 150px; height: 150px;")
        self.timer.singleShot(2000, self.setGreen)

    def setGreen(self):
        self.buttonRed.setStyleSheet("background-color: black; border: 1px solid black; border-radius: 75px; width: 150px; height: 150px;")
        self.buttonYellow.setStyleSheet("background-color: black; border: 1px solid black; border-radius: 75px; width: 150px; height: 150px;")
        self.buttonGreen.setStyleSheet("background-color: green; border: 1px solid black; border-radius: 75px; width: 150px; height: 150px;")
        self.timer.singleShot(2000, self.setYellow)

    def setYellow(self):
        self.buttonYellow.setStyleSheet("background-color: yellow; border: 1px solid black; border-radius: 75px; width: 150px; height: 150px;")
        self.buttonGreen.setStyleSheet("background-color: black; border: 1px solid black; border-radius: 75px; width: 150px; height: 150px;")
        self.timer.singleShot(2000, self.setRed)

app = QApplication(sys.argv)
window = MainWIdget()
window.show()

sys.exit(app.exec())

```