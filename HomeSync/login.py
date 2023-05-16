from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.core.image import Image as CoreImage
from kivy.graphics import Canvas
from kivy.graphics import Rectangle


class LoginScreen(Screen):
    import os
    print(os.getcwd())

    Builder.load_file('login.kv')
    Builder.load_file('signup.kv')
    username_input = ObjectProperty(None)
    password_input = ObjectProperty(None)

    def login(self):
        print("Login with username:", self.username_input.text, "and password:", self.password_input.text)

    def sign_up(self):
        from login import LoginScreen
        self.manager.add_widget(LoginScreen(name='login'))
        self.manager.current = 'login'

    def switch_screen(self, button):
        if button.text == "Login":
            self.manager.current = 'home'
        elif button.text == "Don't have an account? Sign up":
            self.manager.current = 'signup'
        
