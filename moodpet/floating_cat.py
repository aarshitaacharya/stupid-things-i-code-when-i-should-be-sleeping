from PySide6.QtWidgets import QWidget, QLabel, QApplication
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtCore import Qt, QTimer, QPoint
import random
import pygetwindow as gw

class FloatingCat(QWidget):
    def __init__(self, on_click_callback, parent_geometry = None):
        super().__init__()
        self.on_click_callback = on_click_callback

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("cat.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.resize(64, 64)

        if parent_geometry is None:
            parent_geometry = QApplication.primaryScreen().availableGeometry()
        
        self.bounds = parent_geometry

        self.vx = 2
        self.vy = 1
        self.timer = QTimer()
        self.timer.timeout.connect(self.move_random)
        self.timer.start(500)
    
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.hide()
            self.on_click_callback()

    def move_random(self):
        new_x = self.x() + self.vx
        new_y = self.y() + self.vy

        # bounce off horizontal edges
        if new_x < self.bounds.x() or new_x + self.width() > self.bounds.x() + self.bounds.width():
            self.vx = -self.vx
            new_x = max(self.bounds.x(), min(new_x, self.bounds.x() + self.bounds.width() - self.width()))

        # bounce off vertical edges
        if new_y < self.bounds.y() or new_y + self.height() > self.bounds.y() + self.bounds.height():
            self.vy = -self.vy
            new_y = max(self.bounds.y(), min(new_y, self.bounds.y() + self.bounds.height() - self.height()))

        self.move(new_x, new_y)

