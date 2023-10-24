from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

class BedroomScreen(Screen):
    Builder.load_file('bedroom.kv')
