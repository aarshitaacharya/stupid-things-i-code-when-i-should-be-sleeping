from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

class FloatingCat(QWidget):
    def __init__(self, on_click_callback):
        super().__init__()
        self.on_click_callback = on_click_callback

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("cat.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.resize(64, 64)
    
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.on_click_callback()
