from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

class FaqsScreen(Screen):
    Builder.load_file('faqs.kv')
    