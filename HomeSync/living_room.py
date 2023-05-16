from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock

class LivingRoomScreen(Screen):
    Builder.load_file('living_room.kv')
    light_switch = ObjectProperty(None)
    fan_switch = ObjectProperty(None)
    fan_slider = ObjectProperty(None)
    fan_label = ObjectProperty(None)
