from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.animation import Animation    
from kivy.properties import ObjectProperty, BooleanProperty, NumericProperty
from kivy.metrics import dp
from kivy.graphics import Canvas
from kivy.graphics import Rectangle
from kivy.network.urlrequest import UrlRequest
from database_code import *
import socket
from imp_fns import *
from living_room import LivingRoomScreen
from kitchen import KitchenScreen
from dining_room import DiningRoomScreen
from bedroom import BedroomScreen
from login import LoginScreen
import time

class HomeScreen(Screen):
    Builder.load_file('home.kv')
    Builder.load_file('myprofile.kv')
    menu_active = BooleanProperty(False)
    menu_width = NumericProperty(dp(250))

    def toggle_menu(self):
        self.menu_active = not self.menu_active
        #menu_width = self.width
        if self.menu_active:
            Animation(width= 0, d=0.2).start(self.ids.menu)
            #self.ids.menu.pos = (0, 0.5)
        else:
            Animation(width=self.menu_width, d=0.2).start(self.ids.menu)

    def on_enter(self, *args):
        # Reset menu state when entering LoginScreen
        home_screen = self.manager.get_screen('home')
        home_screen.menu_active = False
        home_screen.ids.menu.width = self.menu_width


    def log_out(self) :
        # led0 = LivingRoomScreen().ids.light_switch.active
        # print(led0)
        # fan = LivingRoomScreen().ids.fan_switch.active
        # print(fan)
        
        # led1 = KitchenScreen().ids.light_switch.active
        # print(led1)
        
        # led2 = DiningRoomScreen().ids.light_switch.active
        # print(led2)
        
        # led3 = BedroomScreen().ids.light_switch.active
        # print(led3)
        
        # fan_speed = LivingRoomScreen().ids.fan_label.text
        # print(fan_speed)

        # x = LoginScreen().username_input
        # print(x)
        # # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

        # database.child("Users").child(x).update({
        #     "LED0": int(led0),
        #     "LED1": int(led1),
        #     "LED2": int(led2),
        #     "LED3": int(led3),
        # })
        
        # print("ERROR: Status was not saved!")
        
            #self.ids.menu.pos = (-self.menu_width, 0.5)
    #def toggle_menu(self):
    #    menu = self.ids.menu
    #    menu_width = menu.width
   #     if menu.x == -menu_width:
            # menu is currently hidden, so slide it in
    #        Animation(x=0, duration=0.2).start(menu)
    #    else:
            # menu is currently shown, so slide it out
    #        Animation(x=-menu_width, duration=0.2).start(menu)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.43.37', 80))

        # Send data from Kivy app to ESP32
        data_to_send = "http://192.168.43.37/exit" 
        s.send(data_to_send.encode())
        # time.sleep(5)
        # Receive the response from ESP32
        response = s.recv(1024).decode()
        s.close()
        print(response)

        response = response.split("/")[:-1]
        
        data = {
        "LED0": response[0],
        "LED1": response[1],
        "LED2": response[2],
        "LED3": response[3],
        "FAN_STAT": response[4],
        }

        database.child("Users").child(response[5]).update(data)

    

    



    