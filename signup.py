from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
import requests


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

            #url = 'http://<ESP32_SERVER_IP_ADDRESS>/signup_endpoint' 
            # Replace with your actual server URL
            #response = requests.post(url, json=signup_data)

            # Handle the server response
            #if response.status_code == 200:
                # Successful signup
            #    self.manager.current = 'login'
            #else:
                # Failed signup
            #    self.ids.status_label.text = 'Signup failed. Please try again.'

        elif button.text == "Already have an account? Sign in":
            self.manager.current = 'login'


'''    def signup(self):
        first_name = self.first_name_input.text
        last_name = self.last_name_input.text
        username = self.username_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirm_password = self.confirm_password_input.text

        if password == confirm_password:
            account_data = {
                'First Name': first_name,
                'Last Name': last_name,
                'Username': username,
                'Email': email,
                'Password': password
            }

            self.write_to_csv(account_data)
            self.clear_inputs()
            self.ids.status_label.text = "Account created successfully!"
        else:
            self.ids.status_label.text = "Passwords do not match!"

    def write_to_csv(self, data):
        fieldnames = ['First Name', 'Last Name', 'Username', 'Email', 'Password']
        filename = 'user_data.csv' 

        with open(filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if file.tell() == 0: 
                writer.writeheader()

            writer.writerow(data)

    def clear_inputs(self):
        self.first_name_input.text = ''
        self.last_name_input.text = ''
        self.username_input.text = ''
        self.email_input.text = ''
        self.password_input.text = ''
        self.confirm_password_input.text = ''

'''        

    

        