from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

class LivingRoomScreen(Screen):
    Builder.load_file('living_room.kv')
    light_switch = ObjectProperty(None)
    fan_switch = ObjectProperty(None)
    fan_slider = ObjectProperty(None)
    fan_label = ObjectProperty(None)
