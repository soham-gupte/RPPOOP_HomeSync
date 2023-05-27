from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

class MyProfile(Screen):
    Builder.load_file('myprofile.kv')
    def on_enter(self, *args):
        self.ids.first_name_label.text = "John"  # Replace with your variable containing first name
        self.ids.last_name_label.text = "Doe"  # Replace with your variable containing last name
        self.ids.email_label.text = "johndoe@example.com"  # Replace with your variable containing email
        self.ids.username_label.text = "johndoe"  # Replace with your variable containing username
        self.ids.password_label.text = "********"  # Replace with your variable containing password

    
    
    #def __init__(self, **kwargs):
    #    super().__init__(**kwargs)
        # Initialize user information
    #    self.username = "JohnDoe"
    #    self.password = "password"
    #    self.email = "johndoe@example.com"

    #def on_enter(self, *args):
        # Update user information whenever the screen is displayed
    #    self.ids.username_label.text = self.username
    #    self.ids.password_label.text = self.password
    #    self.ids.email_label.text = self.email