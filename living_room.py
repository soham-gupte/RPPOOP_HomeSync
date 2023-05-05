from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty

class LivingRoomScreen(Screen):
    Builder.load_file('living_room.kv')
    light_switch = ObjectProperty(None)
    fan_switch = ObjectProperty(None)
    fan_slider = ObjectProperty(None)
    fan_label = ObjectProperty(None)

    def on_fan_slider_value(self, instance, value):
        pass
        #self.fan_label.text = str(int(value))

    #def on_enter(self, *args):
    #    pass
        #self.light_switch.disabled = False
        #self.fan_switch.disabled = False

    #def toggle_light(self):
    #    pass
        #if self.light_switch.disabled:
        #    print("Light turned off")
        #else:
        #    print("Light turned on")

    #def on_switch_active(self, widget):
     #   pass
        #print("Switch: " + str(widget.active))

    #def on_slider_value(self, widget):
     #   pass
        #print("Slider: " + str(int(widget.value)))
        #self.slider_value_txt= str(int(widget.value)) 
    
    #def on_text_validate(self, widget):
    #    self.text_input_str= widget.text 

    #def toggle_fan(self):
    #    if self.fan_switch.disabled:
    #        print("Fan turned off")
    #    else:
    #        print("Fan turned on")

    #def on_fan_switch_active(self, instance, value):
    #    self.fan_slider.disabled = not value

    #def on_fan_slider_value(self, instance, value):
    #    print("Fan speed set to:", value)