from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton, QScrollArea
from PySide6.QtCore import Qt
from moodpet import mood_detect, RESPONSES, get_past_mood, save_mood
import random

def send_message():
    text = user_input.text().strip()
    if not text:
        return
    
    mood = mood_detect(text)
    
    user_msg = QLabel(f"You: {text}")
    user_msg.setStyleSheet("background-color: #ff80ab; border-radius: 10px; padding: 5px; max-width: 200px")
    user_msg.setAlignment(Qt.AlignRight)
    chat_layout.addWidget(user_msg)

    pet_msg = QLabel(f"🐰: {random.choice(RESPONSES[mood])}")
    pet_msg.setStyleSheet("background-color: #6a1b9a; color:white; border-radius: 10px; padding: 5px; max-width: 200px;")
    pet_msg.setAlignment(Qt.AlignLeft)
    chat_layout.addWidget(pet_msg)
    
    save_mood(mood)

    user_input.clear()

app = QApplication([])
window = QWidget()
window.setWindowTitle("MoodPet 🐰")

layout = QVBoxLayout()

chat_container = QWidget()
chat_layout = QVBoxLayout()
chat_container.setLayout(chat_layout)

scroll_area = QScrollArea()
scroll_area.setWidget(chat_container)
scroll_area.setWidgetResizable(True)
layout.addWidget(scroll_area)

initial_msg = QLabel(f"🐰: Hi! Last time you felt {get_past_mood()}")
initial_msg.setStyleSheet("background-color: #6a1b9a; color: white; border-radius: 10px; padding: 5px; max-width: 200px")
initial_msg.setAlignment(Qt.AlignLeft)
chat_layout.addWidget(initial_msg)

user_input = QLineEdit()
layout.addWidget(user_input)

send_button = QPushButton("send")
layout.addWidget(send_button)
send_button.clicked.connect(send_message)

window.setLayout(layout)
window.show()
app.exec()

