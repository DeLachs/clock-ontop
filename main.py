from datetime import datetime
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout


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
    widget.setWindowFlags(widget.windowFlags() | Qt.WindowStaysOnTopHint)
    widget.setWindowFlags(widget.windowFlags() & ~Qt.WindowMinMaxButtonsHint)
    widget.show()

    # Refresh label every second
    timer = QTimer()
    timer.timeout.connect(current_time)
    timer.start(1000)  # every 10,000 milliseconds

    app.exec()
