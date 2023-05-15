from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.animation import Animation    
from kivy.properties import ObjectProperty, BooleanProperty, NumericProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from living_room import LivingRoomScreen
from kivy.uix.popup import Popup
from kivy.metrics import dp

class HomeScreen(Screen):
    Builder.load_file('home.kv')
    menu_active = BooleanProperty(False)
    menu_width = NumericProperty(dp(250))

    def toggle_menu(self):
        self.menu_active = not self.menu_active
        menu_width = self.width
        if self.menu_active:
            Animation(width=self.menu_width, d=0.2).start(self.ids.menu)
        else:
            Animation(width= 0, d=0.2).start(self.ids.menu)
    #def toggle_menu(self):
    #    menu = self.ids.menu
    #    menu_width = menu.width
   #     if menu.x == -menu_width:
            # menu is currently hidden, so slide it in
    #        Animation(x=0, duration=0.2).start(menu)
    #    else:
            # menu is currently shown, so slide it out
    #        Animation(x=-menu_width, duration=0.2).start(menu)

    

    



    