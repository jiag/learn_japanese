# -*- coding:utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import (
    ListProperty, NumericProperty, StringProperty, BooleanProperty)
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.dictadapter import ListAdapter
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.popup import Popup
from kivy.app import App


class screen_mainpage(Screen):
    background_color = ListProperty([0.85, 0.95, 0.85, 0.8])
    background_color_secondary = ListProperty([0, 1, 1, 1])
    font_color = ListProperty([0.35, 0.35, 1, 1])
    font_color_secondary = ListProperty([1, 1, 1, 1])
    font_color_title = ListProperty([0, 0, 0.7, 1])
    score=StringProperty("Score: 0")

    def __init__(self, *args, **kwargs):
        super(screen_mainpage, self).__init__(*args, **kwargs)

    def getscores(self):
        return self.score
