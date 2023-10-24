from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

class SignupScreen(Screen):
    Builder.load_file('signup.kv')
    first_name_input = ObjectProperty(None)
    last_name_input = ObjectProperty(None)
    username_input = ObjectProperty(None)
    email_input = ObjectProperty(None)
    password_input = ObjectProperty(None)
    confirm_password_input = ObjectProperty(None)

    def switch_screen(self, button):
        if button.text == "Submit":
            first_name = self.first_name_input.text
            last_name = self.last_name_input.text
            username = self.username_input.text
            email = self.email_input.text
            password = self.password_input.text
            confirm_password = self.confirm_password_input.text

            #input validation

            signup_data = {
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'email': email,
                'password': password
            }

        elif button.text == "Already have an account? Sign in":
            self.manager.current = 'login'


        