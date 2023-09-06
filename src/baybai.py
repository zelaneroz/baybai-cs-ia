import kivy.metrics
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import sqlite3
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
Window.size = (375,812)
from kivy.core.text import LabelBase
#https://zavoloklom.github.io/material-design-iconic-font/icons.html#new
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.textfield import  MDTextField
from syllabify import translate, syllabify
import pyperclip
from kivy.clock import Clock
#klkhjgfgh

class HomeScreen(MDScreen):
    dialog=None

    def home2learn(self):
        self.parent.current = "LearnScreen"
    def home2test(self):
        self.parent.current = "TestScreen"
    def home2translate(self):
        self.parent.current = "TranslateScreen"
    def home2stats(self):
        self.parent.current = "StatsScreen"


class LearnScreen(MDScreen):
    pass

class Flashcards(MDScreen):
    def backtohome(self):
        baybai.backtohome(self)

class TestScreen(MDScreen):
    dialog=None

class TranslateScreen(MDScreen):
    #ADD ERROR MESSAGE FOR WHEN WORD IS NOT TAGALOG.
    dialog=None
    def translate(self):
        # self.ids.translation.text=str(self.ids.tbd.text)
        self.ids.translation.text = str(translate(str(self.ids.tbd.text)))

    def dismiss_popup(self,dt):
        self.dialog.dismiss()
    def copy_translation(self):
        def popup():
            if self.ids.translation.text == '':
                self.dialog = MDDialog(text="Clipboard empty. Please enter a word to be translated")
            else:
                self.dialog = MDDialog(text="Baybayin script copied to clipboard!")
            self.dialog.open()
            Clock.schedule_once(self.dismiss_popup,1)
        pyperclip.copy(str(self.ids.translation.text))
        popup()

    def backtohome(self):
        baybai.backtohome(self)

class StatsScreen(MDScreen):
    dialog=None

class stats(MDScreen):
    dialog=None

class baybai(MDApp):
    def backtohome(self):
        self.parent.current='HomeScreen'
    def build(self):
        LabelBase.register(name='Helvetica',fn_regular='fonts/HelveticaNeue-01.ttf',fn_bold='fonts/HelveticaNeue-Bold-02.ttf',fn_bolditalic='fonts/HelveticaNeue-BoldItalic-04.ttf',fn_italic='fonts/HelveticaNeue-Italic-03.ttf')
        LabelBase.register(name='Baybayin', fn_regular='fonts/Baybayin.ttf')
        LabelBase.register(name='Noto', fn_regular='fonts/NotoSansTagalog.ttf')
        return


test = baybai()
test.run()