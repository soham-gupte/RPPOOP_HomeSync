from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class SettingsScreen(Screen):
    Builder.load_file('settings.kv')
    def toggle_notifications(self, value):
        if value:
            print("Notifications on")
        else:
            print("Notifications off")