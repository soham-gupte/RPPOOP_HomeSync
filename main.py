from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from kivy.lang.builder import Builder
from login import LoginScreen
from signup import SignupScreen
from home import HomeScreen
from living_room import LivingRoomScreen
from kitchen import KitchenScreen
from dining_room import DiningRoomScreen
from bedroom import BedroomScreen
from myprofile import MyProfile
from settings import SettingsScreen
from faqs import FaqsScreen
from atp import AtpScreen
from new import new
from kivy.graphics import Canvas, Rectangle
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.core.window import Window
import csv

'''filename = 'user_data.csv'  
with open(filename, 'w', newline='') as file:
    pass
print(f"Empty CSV file '{filename}' created.")'''

class HomeSync(App):

    def build(self):
        Window.size = (430, 800)
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(LivingRoomScreen(name='living_room'))
        sm.add_widget(KitchenScreen(name= 'kitchen'))
        sm.add_widget(DiningRoomScreen(name= 'dining_room'))
        sm.add_widget(BedroomScreen(name= 'bedroom'))
        sm.add_widget(MyProfile(name= 'myprofile'))
        sm.add_widget(SettingsScreen(name= 'settings'))
        sm.add_widget(FaqsScreen(name= 'faqs'))
        sm.add_widget(AtpScreen(name= 'atp'))
        return sm
    
if __name__ == '__main__':
    HomeSync().run()

