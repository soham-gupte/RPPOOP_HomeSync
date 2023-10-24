from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.animation import Animation
from kivy.properties import ObjectProperty, BooleanProperty, NumericProperty
from kivy.metrics import dp
import json
from kivy.properties import StringProperty
from kivy.uix.spinner import Spinner
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

def open_theme_spinner_dropdown(self):
        # This method will open the dropdown for the theme spinner
        theme_spinner = self.ids.theme_spinner
        theme_spinner.is_open = True

class MySpinnerOption(Button):
    pass

class MySpinner(Spinner):
    dropdown_cls = "MySpinnerDropdown"

class MySpinnerDropdown(DropDown):
    pass

class HomeScreen(Screen):
    Builder.load_file('home.kv')
    Builder.load_file('myprofile.kv')
    menu_active = BooleanProperty(False)
    menu_width = NumericProperty(dp(250))

    theme = StringProperty("Default")

    background_image = StringProperty("images/grad2.jpg")

    kitchen_light_switch = ObjectProperty(None)
    living_room_light_switch = ObjectProperty(None)
    dining_room_light_switch = ObjectProperty(None)
    bedroom_light_switch = ObjectProperty(None)
    living_room_fan_switch = ObjectProperty(None)
    light_switch = ObjectProperty(None)

    def on_dropdown_select(self, selected_option):
        if selected_option == "Dark":
            self.background_image = "images/dark.jpg"
        elif selected_option == "Light":
            self.background_image = "images/light.jpg"
        elif selected_option == "Default":
            self.background_image = "images/grad2.jpg"

    '''def on_start(self):
        # Load the initial theme from themes.json
        with open("themes.json", "r") as theme_file:
            themes = json.load(theme_file)
        initial_theme = themes.get("default")  # You can set your default theme here
        if initial_theme:
            # Apply the initial theme to the HomeScreen
            home_screen = self.root.get_screen("home")
            home_screen.theme = "default"  # Set the initial theme name
            home_screen.load_theme()

    def load_theme(self):
        # Define themes in a dictionary with properties
        themes = {
        "Default": {
            "background_color": [1, 1, 1, 1],
            "text_color": [0, 0, 0, 1],
            "button_color": [0.65, 0.68, 0.96, 1],
            "button_size_hint": [None, None],
            "button_font_size": dp(20),
            "button_width": dp(150),
            "button_height": dp(50),
            "button_background_color": [0.65, 0.68, 0.96, 0.8],
            "button_color": [1, 1, 1, 1],
            "background_image": "images/grad2.jpg",

        },
        "Dark": {
            "background_color": [0, 0, 0, 1],
            "text_color": [1, 1, 1, 1],
            "button_color": [0.2, 0.2, 0.2, 1],
            "background_image": "images/dark.jpg"
        },
        "Green": {
            "background_color": [0.1, 0.3, 0.1, 1],
            "text_color": [1, 1, 1, 1],
            "button_color": [0.1, 0.5, 0.1, 1],
            "background_image": "images/light.jpg",
        }
    }

        # Get the theme dictionary based on the selected theme name
        theme_data = themes.get(self.theme)

        # Apply the theme to widgets
        if theme_data:
            self.ids.background_image.source = theme_data["background_color"]
            self.ids.my_label.color = theme_data["text_color"]
            self.ids.my_button.background_color = theme_data["button_color"]

    def set_theme(self, theme_name):
        self.theme = theme_name
        self.load_theme()
'''
    def master_off(self):
        # Control all light switches to turn them off
        for screen_name in ['kitchen', 'living_room', 'dining_room', 'bedroom']:
            screen = self.manager.get_screen(screen_name)
            light_switch = screen.ids.light_switch

            if light_switch:
                light_switch.active = False

        # Handle the living room fan switch separately
        living_room_fan_switch = self.manager.get_screen('living_room').ids.fan_switch
        if living_room_fan_switch:
            living_room_fan_switch.active = False

    def toggle_menu(self):
        self.menu_active = not self.menu_active
        if self.menu_active:
            Animation(width=0, d=0.2).start(self.ids.menu)
        else:
            Animation(width=self.menu_width, d=0.2).start(self.ids.menu)

    def on_enter(self, *args):
        # Reset menu state when entering LoginScreen
        home_screen = self.manager.get_screen('home')
        home_screen.menu_active = False
        home_screen.ids.menu.width = self.menu_width
