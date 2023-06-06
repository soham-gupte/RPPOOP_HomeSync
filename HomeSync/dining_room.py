from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.switch import Switch
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.network.urlrequest import UrlRequest
from database_code import *

class DiningRoomScreen(Screen):
    light_switch = ObjectProperty(None)
    Builder.load_file('dining_room.kv')

    def toggle_light(self):
        x = LED_URL + "2"
        UrlRequest(x)
