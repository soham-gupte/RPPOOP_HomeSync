from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty


class SignupScreen(Screen):
    Builder.load_file('signup.kv')
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    username_signup = ObjectProperty(None)
    password_signup = ObjectProperty(None)
    confirm_password_signup = ObjectProperty(None)

    def signup(self):
        print("Signup with first name:", self.first_name.text, "last name:", self.last_name.text, "username:", self.username_signup.text, "password:", self.password_signup.text, "confirm password:", self.confirm_password_signup.text)

    def switch_screen(self, button):
        if button.text == "Submit":
            self.manager.current = 'login'
        elif button.text == "Already have an account? Sign in":
            self.manager.current = 'login'
        