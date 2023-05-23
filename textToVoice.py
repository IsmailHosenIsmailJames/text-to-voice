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
    "Urdu": "ur",
    "Ukrainian": "uk",
    "Kannada": "kn",
    "Greek": "el",
    "Afrikaans": "af",
}

ShowLangaugeName = [
    "Bengali",
    "Afrikaans" "Arabic",
    "Chinese",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Japanese",
    "Kannada",
    "Korean",
    "Portuguese",
    "Polish",
    "Russian",
    "Swedish",
    "Spanish",
    "Turkish",
    "Urdu",
    "Ukrainian",
    "Vietnamese",
]


def submit_text():
    global defultLanguage
    print(defultLanguage)
    text = text_field.toPlainText()
    tts = gtts.gTTS(text=text, lang=defultLanguage)
    if len(text) > 20:
        text = text[0:20]
    fileName = f"{text}.mp3"
    tts.save(fileName)
    os.system(fileName)
    playsound.playsound(fileName, True)


def handle_dropdown_selection(index):
    global defultLanguage
    selected_option = combo_box.itemText(index)
    defultLanguage = dictionaryForGetShortFrom[selected_option]


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
window.setWindowTitle("Text to Voice")
window.show()

sys.exit(app.exec())
