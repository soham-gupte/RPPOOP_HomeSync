from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.animation import Animation
from kivy.properties import ObjectProperty, BooleanProperty, NumericProperty
from kivy.metrics import dp
from kivy.properties import StringProperty

class HomeScreen(Screen):
    Builder.load_file('home.kv')
    Builder.load_file('myprofile.kv')
    menu_active = BooleanProperty(False)
    menu_width = NumericProperty(dp(250))

    background_image = StringProperty("images/grad2.jpg")

    kitchen_light_switch = ObjectProperty(None)
    living_room_light_switch = ObjectProperty(None)
    dining_room_light_switch = ObjectProperty(None)
    bedroom_light_switch = ObjectProperty(None)
    living_room_fan_switch = ObjectProperty(None)
    light_switch = ObjectProperty(None)

    def on_dropdown_select(self, selected_option):
        if selected_option == "Dark":
            self.app.set_selected_background("images/dark.jpg")
        elif selected_option == "Light":
            self.app.set_selected_background("images/light.jpg")
        elif selected_option == "Default":
            self.app.set_selected_background("images/grad2.jpg")

    def master_off(self):
        for screen_name in ['kitchen', 'living_room', 'dining_room', 'bedroom']:
            screen = self.manager.get_screen(screen_name)
            light_switch = screen.ids.light_switch

            if light_switch:
                light_switch.active = False

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
        home_screen = self.manager.get_screen('home')
        home_screen.menu_active = False
        home_screen.ids.menu.width = self.menu_width
