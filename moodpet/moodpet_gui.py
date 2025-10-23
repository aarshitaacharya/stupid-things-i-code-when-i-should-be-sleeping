from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton
from moodpet import mood_detect, RESPONSES
import random

def send_message():
    text = user_input.text().strip()
    if not text:
        return
    
    mood = mood_detect(text)
    chat_log.append(f"You: {text}")
    chat_log.append(f"🐰: {random.choice(RESPONSES[mood])}")

app = QApplication([])
window = QWidget()
window.setWindowTitle("MoodPet 🐰")

layout = QVBoxLayout()

title_label = QLabel("Hi! I'm MoodPet 🐰")
layout.addWidget(title_label)

chat_log = QTextEdit()
chat_log.setReadOnly(True)
layout.addWidget(chat_log)

user_input = QLineEdit()
layout.addWidget(user_input)

send_button = QPushButton("send")
layout.addWidget(send_button)
send_button.clicked.connect(send_message)

window.setLayout(layout)
window.show()
app.exec()

