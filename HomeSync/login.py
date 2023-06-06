from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
# from kivy.properties import TextInput
from kivy.core.image import Image as CoreImage
from kivy.graphics import Canvas
from kivy.graphics import Rectangle
# import requests
from kivy.uix.textinput import TextInput
import socket
from imp_fns import *
import time
from living_room import LivingRoomScreen
from kitchen import KitchenScreen
from dining_room import DiningRoomScreen
from bedroom import BedroomScreen

class LoginScreen(Screen):


    Builder.load_file('login.kv')
    Builder.load_file('signup.kv')
    username_input = ObjectProperty(TextInput())
    password_input = ObjectProperty(TextInput()) 

    def login(self):
        if (not check_internet_connection()) :
            self.ids.status_label.text = "PLEASE CONNECT TO THE INTERNET!"
            return
        else :
            if (not check_connection_with_esp()) :
                self.ids.status_label.text = "CONNECT TO SAME WIFI!"
                return
            else :
                # self.ids.status_label.text = "Connection successful!"
                pass
        
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        self.username_input = username

        if not check_login(username, password) :
            self.ids.status_label.text = "Invalid credentials! Please try again."
            return
        
        print("Login with username:", username, "and password:", password)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.43.37', 80))

        # Send data from Kivy app to ESP32
        data_to_send = "http://192.168.43.37/" + username + "/" + password 
        s.send(data_to_send.encode())

        # Receive the response from ESP32
        response = s.recv(1024).decode()

        # Close the socket connection
        s.close()
        print(response)

        if int(response) :
            # self.ids.status_label.text = "Login succesful!"
            time.sleep(0.5)
            self.manager.current = 'home'