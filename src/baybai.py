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

#ICONS: https://zavoloklom.github.io/material-design-iconic-font/icons.html#new

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
    dialog=None

class TestScreen(MDScreen):
    dialog=None

class TranslateScreen(MDScreen):
    dialog=None

class StatsScreen(MDScreen):
    dialog=None

class baybai(MDApp):
    def build(self):
        return

test = baybai()
test.run()