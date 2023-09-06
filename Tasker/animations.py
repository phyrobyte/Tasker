from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QPushButton

def animate_button(button: QPushButton, min_height=30, max_height=40, duration=1000):
    """Animate a button to bob up and down."""
    animation = QPropertyAnimation(button, b"minimumHeight")
    animation.setDuration(duration)
    animation.setStartValue(min_height)
    animation.setEndValue(max_height)
    animation.setEasingCurve(QEasingCurve.InOutSine)
    animation.setLoopCount(-1)
    return animation

def stop_animation(animation):
    """Stop a running animation."""
    animation.stop()
