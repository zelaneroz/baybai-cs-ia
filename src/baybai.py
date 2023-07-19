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

class HomeScreen(MDScreen):
    dialog=None

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