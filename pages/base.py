from kivy.uix.screenmanager import Screen
from kivy.app import App

class BaseScreen(Screen):
    @property
    def root(self):
        return App.get_running_app().root