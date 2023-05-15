from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from signup import SignupScreen
from home import HomeScreen

class LoginScreen(Screen):
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
        elif button.text == "Sign up":
            self.manager.current = 'signup'
        
