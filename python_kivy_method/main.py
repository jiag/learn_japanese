# -*- coding:utf-8 -*-
from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import (ListProperty, NumericProperty, ObjectProperty,
                             StringProperty, BooleanProperty)
from kivy.adapters.dictadapter import ListAdapter
from kivy.uix.button import Button
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.clock import Clock
from datetime import datetime
from kivy.lang import Builder

import sys
from screen_mainpage import screen_mainpage

Builder.load_file('screen_mainpage.kv')



class LearnJapanese_ScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(LearnJapanese_ScreenManager, self).__init__(**kwargs)
        self.add_widget(screen_mainpage(name="mainpage"))
        self.current = 'mainpage'


class LearnJapaneseApp(App):

    def build(self):
        self.sm = LearnJapanese_ScreenManager()
        return self.sm

if __name__ == "__main__":
    LearnJapaneseApp().run()
