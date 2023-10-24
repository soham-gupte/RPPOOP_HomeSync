from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

class SettingsScreen(Screen):
    Builder.load_file('settings.kv')
    def toggle_notifications(self, value):
        if value:
            print("Notifications on")
        else:
            print("Notifications off")

