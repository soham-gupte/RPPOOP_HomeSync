from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.core.image import Image as CoreImage
import requests


class LoginScreen(Screen):
    import os
    print(os.getcwd())

    Builder.load_file('login.kv')
    Builder.load_file('signup.kv')
    username_input = ObjectProperty(None)
    password_input = ObjectProperty(None)

    def login(self):
        username = self.username_input.text
        password = self.password_input.text
        login_data = {
            'username': username,
            'password': password
        }

        url = 'http://<ESP32_SERVER_IP_ADDRESS>/login_endpoint'  # Replace with your actual server URL
        response = requests.post(url, json=login_data)

        # Handle the server response
        if response.status_code == 200:
            # Successful login
            self.manager.current = 'home'
        else:
            # Failed login
            self.ids.status_label.text = 'Invalid credentials. Please try again.'

    def sign_up(self):
        from login import LoginScreen
        self.manager.add_widget(LoginScreen(name='login'))
        self.manager.current = 'login'

    def switch_screen(self, button):
        if button.text == "Login":
            self.manager.current = 'home'
        elif button.text == "Don't have an account? Sign up":
            self.manager.current = 'signup'
        
