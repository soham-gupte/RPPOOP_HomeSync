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
from functions import invert_status

SERVER_URL = "http://192.168.43.37/led1"

class BedroomScreen(Screen):
    Builder.load_file('bedroom.kv')

    def toggle_light(self):
        # Send a request to the ESP32 server to toggle the light
        UrlRequest(SERVER_URL)
        invert_status("LED1")
