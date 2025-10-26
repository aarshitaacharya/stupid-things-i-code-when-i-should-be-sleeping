from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton, QScrollArea, QSizePolicy, QHBoxLayout
from PySide6.QtCore import Qt
from moodpet import mood_detect, RESPONSES, get_past_mood, save_mood
import random


class MoodPetChat(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("MoodPet 🐰")
        self.resize(400, 600)
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout()
        self.chat_container = QWidget()
        self.chat_layout = QVBoxLayout()
        self.chat_layout.addStretch()
        self.chat_container.setLayout(self.chat_layout)
        self.chat_container.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.chat_container)
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)

        self.user_input = QLineEdit()
        self.user_input.returnPressed.connect(self.send_message)
        self.layout.addWidget(self.user_input)

        self.send_button = QPushButton("send")
        self.layout.addWidget(self.send_button)
        self.send_button.clicked.connect(self.send_message)

        initial_msg = QLabel(f"🐰: Hi! Last time you felt {get_past_mood()}")
        initial_msg.setStyleSheet("background-color: #6a1b9a; color:white; border-radius:10px; padding:5px;")
        initial_msg.setWordWrap(True)
        container = QWidget()
        row = QHBoxLayout()
        row.addWidget(initial_msg)
        row.addStretch()
        container.setLayout(row)
        self.chat_layout.addWidget(container)

        self.setLayout(self.layout)


    def max_bubble_width(self):
        window_width = self.width()
        max_bubble_width = int(window_width * 0.75)
        if max_bubble_width < 200:
            max_bubble_width = 200
        return max_bubble_width


    def send_message(self):
        text = self.user_input.text().strip()
        if not text:
            return

        mood = mood_detect(text)
        max_px = self.max_bubble_width()

        # --- User bubble ---
        user_msg = QLabel(f"You: {text}")
        user_msg.setWordWrap(True)
        user_msg.setMaximumWidth(max_px)
        user_msg.setStyleSheet("background-color: #ff80ab; border-radius:10px; padding:5px;")
        user_msg.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        user_container = QWidget()
        user_layout = QHBoxLayout()
        user_layout.addStretch()
        user_layout.addWidget(user_msg)
        user_layout.setContentsMargins(0, 0, 0, 0)
        user_container.setLayout(user_layout)
        self.chat_layout.addWidget(user_container)

        # --- MoodPet bubble ---
        pet_msg = QLabel(f"🐰: {random.choice(RESPONSES[mood])}")
        pet_msg.setWordWrap(True)
        pet_msg.setMaximumWidth(max_px)
        pet_msg.setStyleSheet("background-color: #6a1b9a; color:white; border-radius:10px; padding:5px;")
        pet_msg.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        pet_container = QWidget()
        pet_layout = QHBoxLayout()
        pet_layout.addWidget(pet_msg)
        pet_layout.addStretch()
        pet_layout.setContentsMargins(0, 0, 0, 0)
        pet_container.setLayout(pet_layout)
        self.chat_layout.addWidget(pet_container)

        save_mood(mood)
        self.user_input.clear()
        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

if __name__ == "__main__":
    app = QApplication([])
    w = MoodPetChat()
    w.show()
    app.exec()

