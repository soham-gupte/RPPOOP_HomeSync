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

class KitchenScreen(Screen):
    light_switch = ObjectProperty(None)
    Builder.load_file('kitchen.kv')

    def toggle_light(self):
        x = LED_URL + "1"
        UrlRequest(x)

    # def toggle_light(self):
        # Send a request to the ESP32 server to toggle the light
        # UrlRequest(LED1_URL)
        # invert_status("LED0")