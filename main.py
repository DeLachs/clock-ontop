import sys
import time
from datetime import datetime
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QLineEdit, QApplication, QLabel, QWidget, QVBoxLayout, QPushButton
from PySide6.examples.widgets.animation.easing.ui_form import Ui_Form


def current_time():
    now = datetime.now()
    time_string = str(now.strftime("%H:%M:%S"))
    label.setText(time_string)


if __name__ == '__main__':
    app = QApplication([])
    # Change font size
    app.setStyleSheet("QLabel{font-size: 26pt;}")

    # Create label
    label = QLabel(alignment=Qt.AlignCenter)

    # Create layout and add widgets
    layout = QVBoxLayout()
    layout.addWidget(label)

    # Apply layout to widget
    widget = QWidget()
    widget.resize(175, 50)
    widget.setLayout(layout)
    widget.setWindowTitle("Clock")
    # widget.setWindowFlag(Qt.FramelessWindowHint)
    widget.setWindowFlags(widget.windowFlags() | Qt.WindowStaysOnTopHint)
    widget.setWindowFlags(widget.windowFlags() & ~Qt.WindowMinMaxButtonsHint)
    widget.show()

    # Refresh label every second
    timer = QTimer()
    timer.timeout.connect(current_time)
    timer.start(1000)  # every 10,000 milliseconds

    app.exec()
