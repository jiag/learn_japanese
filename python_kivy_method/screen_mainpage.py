# -*- coding:utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import (
    ObjectProperty, ListProperty, NumericProperty, StringProperty, BooleanProperty)
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.dictadapter import ListAdapter
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.behaviors import ( ButtonBehavior, ToggleButtonBehavior)
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label

class IconButton(ButtonBehavior, Image):
#    def __init__(self,*args,**kwargs):
#       super(iconButton,self).__init__(*args,**kwargs)
    pass

class IconToggle(ToggleButtonBehavior, Label):
    pass

class MyDropDown(DropDown):
    pass

class screen_mainpage(Screen):
    background_color = ListProperty([0.85, 0.95, 0.85, 0.8])
    background_color_secondary = ListProperty([0, 1, 1, 1])
    font_color = ListProperty([0.35, 0.35, 1, 1])
    font_color_secondary = ListProperty([1, 1, 1, 1])
    font_color_title = ListProperty([0, 0, 0.7, 1])
    score=StringProperty("Score: 0")
    mode = StringProperty("Reading")
#    sound = StringProperty("Basic Sounds")
#    hika = ObjectProperty(None)
    buttom_layout = ObjectProperty(None)
    dd_btn = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(screen_mainpage, self).__init__(*args, **kwargs)
        self.drop_down = MyDropDown()
        # sounds_choice = DropDown()
        # sounds_type = ['Basic Sounds', 'Modified Sounds I', 'Modified Sounds II', 'All Sounds']
        # for snd in sounds_type:
        #     btn = Button(text='Restart\n'+snd, size_hint_y=None, height=30)
        #     btn.bind(on_release=lambda btn: sounds_choice.select(btn.text))
        #     sounds_choice.add_widget(btn)

        # mainbutton = Button(text = "Restart",size_hint=(None,1))
        # mainbutton.bind(on_release=sounds_choice.open)
        # sounds_choice.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        # self.buttom_layout.add_widget(mainbutton)

    def getscores(self):
        return self.score

    def gotoInfo(self):
        self.parent.current='info'

    def getSounds(self):
        return self.sound

    def hi_or_ka(self):
        if self.hi_ka.state == "down":
            self.hi_ka.text = 'Katakana'
        else:
            self.hi_ka.text = 'Hiragana'
    def modeSwitch(self):
        if self.modes.state == 'down':
            self.modes.text = 'Mode\n Reading'
        else:
            self.modes.text = 'Mode\n Listening'


