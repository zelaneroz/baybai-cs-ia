from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.clock import Clock
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.theming import ThemeManager

# Flashcard data
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    # Add more flashcards here
]

# KV Language
KV = '''
<FlashcardScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDCard:
            id: flashcard_card
            orientation: 'vertical'
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDLabel:
                id: flashcard_label
                text: "Tap to reveal question"
                font_style: 'H5'
                halign: 'center'
                valign: 'center'
        MDRaisedButton:
            text: 'Next Flashcard'
            on_release: root.next_flashcard()

<FlashcardApp>:
    ScreenManager:
        FlashcardScreen:
            name: 'flashcard_screen'
'''

class FlashcardScreen(Screen):
    current_card_index = 0
    revealed = False

    def on_pre_enter(self):
        self.update_card()

    def update_card(self):
        self.revealed = False
        self.ids.flashcard_label.text = "Tap to reveal question"

    def next_flashcard(self):
        self.current_card_index = (self.current_card_index + 1) % len(flashcards)
        self.update_card()

    def on_touch_down(self, touch):
        if self.revealed:
            self.next_flashcard()
        else:
            self.revealed = True
            self.ids.flashcard_label.text = flashcards[self.current_card_index]["question"]


class FlashcardApp(App):
    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    FlashcardApp().run()
