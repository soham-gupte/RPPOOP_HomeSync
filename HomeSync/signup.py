from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
import requests
from kivy.uix.textinput import TextInput
import socket
import time

class SignupScreen(Screen):
    Builder.load_file('signup.kv')
    first_name_input = ObjectProperty(TextInput())
    last_name_input = ObjectProperty(TextInput())
    email_input = ObjectProperty(TextInput())
    username_input = ObjectProperty(TextInput())
    password_input = ObjectProperty(TextInput())
    confirm_password_input = ObjectProperty(TextInput())

    def signup(self):
        #print("Signup with first name:", self.first_name.text, "last name:", self.last_name.text, "username:", self.username_signup.text, "password:", self.password_signup.text, "confirm password:", self.confirm_password_signup.text)
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        confirm_password = self.ids.confirm_password_input.text
        email = self.ids.email_input.text
        first_name = self.ids.first_name_input.text
        last_name = self.ids.last_name_input.text
        
        if len(email) < 10 :
            self.ids.status_label.text = "Email invalid! Try again."
            return
        if len(username) < 8 :
            self.ids.status_label.text = "Username too short, try again!"
            return
        if len(password) < 8 :
            self.ids.status_label.text = "Password too short, try again!"
            return
        if confirm_password != password :
            self.ids.status_label.text = "Password does not match, input password again!"
            return
        
        print("Signup with:-\nusername:", username, "\npassword:", password, "\nemail:", email)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.43.37', 80))
        # Send data from Kivy app to ESP32
        data_to_send = "http://192.168.43.37/signup/" + email + "/" + password + "/" + first_name + "/" + last_name + "/" + username
        s.send(data_to_send.encode())
        # Close the socket connection
        s.close()

        self.ids.status_label.text = "Signup successful, redirecting you to login..."
        time.sleep(0.5)
        self.manager.current = 'login'
    
        