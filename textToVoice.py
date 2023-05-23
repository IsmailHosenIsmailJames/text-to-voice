from PyQt6.QtWidgets import *
import sys
import os
import gtts
import playsound

defultLanguage = "bn"

dictionaryForGetShortFrom = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Hindi": "hi",
    "Bengali": "bn",
    "Dutch": "nl",
    "Greek": "el",
    "Swedish": "sv",
    "Turkish": "tr",
    "Vietnamese": "vi",
    "Polish": "pl",
}

ShowLangaugeName = [
    "Bengali",
    "English",
    "Spanish",
    "French",
    "German",
    "Italian",
    "Portuguese",
    "Russian",
    "Chinese",
    "Japanese",
    "Korean",
    "Arabic",
    "Hindi",
    "Dutch",
    "Greek",
    "Swedish",
    "Turkish",
    "Vietnamese",
    "Polish",
]

def submit_text():
    text = text_field.toPlainText()
    tts = gtts.gTTS(text=text, lang= defultLanguage)
    if len(text) > 20:
        text = text[0:20]
    fileName = f"{text}.mp3"
    tts.save(fileName)
    os.system(f"mpg321 {fileName}")
    playsound.playsound(fileName, True)


def handle_dropdown_selection(index):
    selected_option = combo_box.itemText(index)
    defultLanguage = dictionaryForGetShortFrom[selected_option]
    print(defultLanguage)


app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

text_field = QTextEdit()
submit_button = QPushButton("Submit")
submit_button.clicked.connect(submit_text)
combo_box = QComboBox()
combo_box.addItems(ShowLangaugeName)
combo_box.activated.connect(handle_dropdown_selection)

layout.addWidget(text_field)
layout.addWidget(combo_box)
layout.addWidget(submit_button)

window.setLayout(layout)
window.setWindowTitle("Awesome Interface")
window.show()

sys.exit(app.exec())
