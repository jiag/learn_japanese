# -*- coding:utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import (
    ListProperty, NumericProperty, StringProperty, BooleanProperty)
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.dictadapter import ListAdapter
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.app import App

class IconButton(ButtonBehavior, Image):
#    def __init__(self,*args,**kwargs):
#       super(iconButton,self).__init__(*args,**kwargs)
    pass

class MyToggleButton(ToggleButton):
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
    sound = StringProperty("Basic Sounds")
    hika = StringProperty("Hiragana")
    def __init__(self, *args, **kwargs):
        super(screen_mainpage, self).__init__(*args, **kwargs)
        sounds_choice = MyDropDown()
        mainbutton = Button(text = "Hello!",size_hint=(None,None))
        mainbutton.bind(on_release=sounds_choice.open)

    def getscores(self):
        return self.score

    def gotoInfo(self):
        self.parent.current='info'

    def getSounds(self):
        return self.sound
