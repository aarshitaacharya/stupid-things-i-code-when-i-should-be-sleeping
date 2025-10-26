from PySide6.QtWidgets import QApplication
from moodpet_gui import MoodPetChat
from floating_cat import FloatingCat

app = QApplication([])

chat_window = MoodPetChat()
chat_window.hide()

screen = app.primaryScreen().geometry()

def on_cat_click():
    if chat_window.isVisible():
        chat_window.hide()
    else:
        chat_window.show()
        chat_window.raise_()

cat = FloatingCat(on_click_callback=on_cat_click, parent_geometry=screen)
cat.show()

app.exec()