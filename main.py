from kivy.app import App 
from kivymd.app import MDApp
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from login import LoginScreen
from signup import SignupScreen
from home import HomeScreen
from living_room import LivingRoomScreen
from kitchen import KitchenScreen
from dining_room import DiningRoomScreen
from bedroom import BedroomScreen
from new import new

#Builder.load_file("menu.kv")
#Builder.load_file('homesync.kv')
Builder.load_file('login.kv')
#Builder.load_file('signup.kv')
#Builder.load_file('home.kv')
#Builder.load_file('living_room.kv')
#Builder.load_file('kitchen.kv')
#Builder.load_file('dining_room.kv')
#Builder.load_file('bedroom.kv')

class HomeSync(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(LivingRoomScreen(name='living_room'))
        sm.add_widget(KitchenScreen(name= 'kitchen'))
        sm.add_widget(DiningRoomScreen(name= 'dining_room'))
        sm.add_widget(BedroomScreen(name= 'bedroom'))
        return sm

if __name__ == '__main__':
    HomeSync().run()

