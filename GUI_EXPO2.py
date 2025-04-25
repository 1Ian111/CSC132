from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
from PySide6.QtGui import QPainter, QPen, QColor, QFont
from PySide6.QtCore import Qt, QPoint, QTimer
import sys
import random

class MeshCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.nodes = [QPoint(random.randint(50, 1230), random.randint(50, 600)) for _ in range(45)]  # fit 1280x650
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(80)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), QColor(15, 15, 15))  # dark bg

        # Connections
        pen = QPen(QColor("#00ffff"), 1)
        painter.setPen(pen)
        for i in range(len(self.nodes)):
            for j in range(i+1, len(self.nodes)):
                if random.random() < 0.07:
                    painter.drawLine(self.nodes[i], self.nodes[j])

        # Nodes
        for node in self.nodes:
            painter.setBrush(QColor("#00ffff"))
            painter.drawEllipse(node, 3, 3)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Controller-less Controller")
        self.setFixedSize(1280, 650)

        self.canvas = MeshCanvas()
        self.setCentralWidget(self.canvas)

        # Overlay layout
        overlay = QWidget(self.canvas)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        overlay.setLayout(layout)
        overlay.setGeometry(0, 0, 1280, 650)

        # Title
        title = QLabel("> Welcome to Controller-less Controller <")
        title.setFont(QFont("Consolas", 22, QFont.Bold))
        title.setStyleSheet("color: #39ff14; margin-bottom: 20px;")
        layout.addWidget(title)

        # Button style
        btn_style = """
            QPushButton {
                color: #00ffff;
                background-color: #1a1a1a;
                border: 2px solid #00ffff;
                border-radius: 8px;
                padding: 14px 28px;
                font-family: Consolas;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #111;
                color: #39ff14;
                border-color: #39ff14;
            }
        """

        # Buttons
        for text in ["🖐 Hand Gesture Buttons", "🕺 Full Body Movement", "🖱 Mouse Hand Gesture", "🚪 Quit"]:
            btn = QPushButton(text)
            btn.setStyleSheet(btn_style)
            btn.clicked.connect(QApplication.quit if "Quit" in text else lambda: print(f"{text} clicked"))
            layout.addWidget(btn)

# Run the app
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
