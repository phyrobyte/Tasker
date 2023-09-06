# background.py
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QLinearGradient
from PyQt5.QtCore import QTimer, Qt

class AnimatedBackground(QWidget):
    def __init__(self):
        super().__init__()
        self.color_offset = 0

        # Set up timer for animation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_color)
        self.timer.start(100)  # Update every 100ms

    def update_color(self):
        self.color_offset += 1
        if self.color_offset > 255:
            self.color_offset = 0
        self.update()  # Trigger repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, Qt.red)
        gradient.setColorAt(0.5, Qt.blue)
        gradient.setColorAt(1, Qt.green)
        painter.fillRect(self.rect(), gradient)
