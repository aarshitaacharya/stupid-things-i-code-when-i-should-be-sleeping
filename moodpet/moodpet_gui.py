from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton, QScrollArea, QSizePolicy, QHBoxLayout
from PySide6.QtCore import Qt
from moodpet import mood_detect, RESPONSES, get_past_mood, save_mood
import random

def max_bubble_width():
    window_width = window.width()
    max_bubble_width = int(window_width * 0.75)

    if max_bubble_width < 200:
        max_bubble_width = 200
    
    return max_bubble_width

def send_message():
    text = user_input.text().strip()
    if not text:
        return
    
    mood = mood_detect(text)
    max_px = max_bubble_width()
    
    # User bubble
    user_msg = QLabel(f"You: {text}")
    user_msg.setWordWrap(True)
    user_msg.setMaximumWidth(max_px)
    user_msg.setStyleSheet("background-color: #ff80ab; border-radius:10px; padding:5px;")
    user_msg.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    user_container = QWidget()
    user_layout = QHBoxLayout()
    user_layout.addStretch()
    user_layout.addWidget(user_msg)
    user_layout.setContentsMargins(0,0,0,0)
    user_container.setLayout(user_layout)
    chat_layout.addWidget(user_container)

    # MoodPet bubble
    pet_msg = QLabel(f"🐰: {random.choice(RESPONSES[mood])}")
    pet_msg.setWordWrap(True)
    pet_msg.setMaximumWidth(max_px)
    pet_msg.setStyleSheet("background-color: #6a1b9a; color:white; border-radius:10px; padding:5px;")
    pet_msg.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    pet_container = QWidget()
    pet_layout = QHBoxLayout()
    pet_layout.addWidget(pet_msg)
    pet_layout.addStretch()
    pet_layout.setContentsMargins(0,0,0,0)
    pet_container.setLayout(pet_layout)
    chat_layout.addWidget(pet_container)

    save_mood(mood)
    user_input.clear()
    scroll_area.verticalScrollBar().setValue(scroll_area.verticalScrollBar().maximum())

app = QApplication([])
window = QWidget()
window.setWindowTitle("MoodPet 🐰")
window.resize(400,600)

layout = QVBoxLayout()

chat_container = QWidget()
chat_layout = QVBoxLayout()
chat_layout.addStretch()
chat_container.setLayout(chat_layout)
chat_container.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

scroll_area = QScrollArea()
scroll_area.setWidget(chat_container)
scroll_area.verticalScrollBar().setValue(scroll_area.verticalScrollBar().maximum())
scroll_area.setWidgetResizable(True)
layout.addWidget(scroll_area)

initial_width = max_bubble_width()
initial_msg = QLabel(f"🐰: Hi! Last time you felt {get_past_mood()}")
initial_msg.setWordWrap(True)
initial_msg.setStyleSheet(f"background-color: #6a1b9a; color: white; border-radius: 10px; padding: 5px; max-width: {initial_width}px")
initial_msg.setMaximumWidth(initial_width)
initial_msg.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
initial_container = QWidget()
initial_layout = QHBoxLayout()
initial_layout.addWidget(initial_msg)
initial_layout.addStretch()
initial_container.setLayout(initial_layout)
chat_layout.addWidget(initial_container)

user_input = QLineEdit()
user_input.returnPressed.connect(send_message)
layout.addWidget(user_input)

send_button = QPushButton("send")
layout.addWidget(send_button)
send_button.clicked.connect(send_message)

window.setLayout(layout)
window.show()
app.exec()

