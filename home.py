from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.animation import Animation    
from kivy.properties import ObjectProperty, BooleanProperty, NumericProperty
from kivy.metrics import dp
from kivy.graphics import Canvas
from kivy.graphics import Rectangle

class HomeScreen(Screen):
    Builder.load_file('home.kv')
    Builder.load_file('myprofile.kv')
    menu_active = BooleanProperty(False)
    menu_width = NumericProperty(dp(250))

    def toggle_menu(self):
        self.menu_active = not self.menu_active
        #menu_width = self.width
        if self.menu_active:
            Animation(width= 0, d=0.2).start(self.ids.menu)
            #self.ids.menu.pos = (0, 0.5)
        else:
            Animation(width=self.menu_width, d=0.2).start(self.ids.menu)

    def on_enter(self, *args):
        # Reset menu state when entering LoginScreen
        home_screen = self.manager.get_screen('home')
        home_screen.menu_active = False
        home_screen.ids.menu.width = self.menu_width

            #self.ids.menu.pos = (-self.menu_width, 0.5)
    #def toggle_menu(self):
    #    menu = self.ids.menu
    #    menu_width = menu.width
   #     if menu.x == -menu_width:
            # menu is currently hidden, so slide it in
    #        Animation(x=0, duration=0.2).start(menu)
    #    else:
            # menu is currently shown, so slide it out
    #        Animation(x=-menu_width, duration=0.2).start(menu)

    

    



    