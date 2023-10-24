from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

class DiningRoomScreen(Screen):
    Builder.load_file('dining_room.kv')
