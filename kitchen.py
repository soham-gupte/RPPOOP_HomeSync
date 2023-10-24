from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

class KitchenScreen(Screen):
    Builder.load_file('kitchen.kv')

    