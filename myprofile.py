from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

class MyProfile(Screen):
    Builder.load_file('myprofile.kv')
    def on_enter(self, *args):
        self.ids.first_name_label.text = "John"  # Replace with your variable containing first name
        self.ids.last_name_label.text = "Doe"  # Replace with your variable containing last name
        self.ids.email_label.text = "johndoe@example.com"  # Replace with your variable containing email
        self.ids.username_label.text = "johndoe"  # Replace with your variable containing username
        self.ids.password_label.text = "********"  # Replace with your variable containing password
