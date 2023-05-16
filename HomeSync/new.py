from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.switch import Switch
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.image import Image

class new(Screen):
    Builder.load_file('new.kv')

    