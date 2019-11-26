from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.clock import Clock
from kivy.uix.screenmanager import NoTransition, SlideTransition
import json

class MainNavigationLayout(NavigationLayout):
    def __init__(self, *args, **kwargs):
        NavigationLayout.__init__(self, *args, **kwargs)
        self._panel_disable = True

        Clock.schedule_once(self.check_logged)

    def get_data(self):
        f = open("data.json", "rb")
        f_data = f.read().decode()
        data = json.loads(f_data)
        f.close()
        return data

    def set_data(self, key, value):
        data = self.get_data()
        data[key] = value
        f = open("data.json", "wb")
        f.write(json.dumps(data).encode())

    def check_logged(self, *args):
        data = self.get_data()
        if data['logged'] == "True":
            m = self.ids.screen_manager
            m.transition = NoTransition()

            self.ids.screen_manager.current = "screen_inicio"
            self.enable_drawer()
            m.transition = SlideTransition()

    def enable_drawer(self):
        self.ids.w_toolbar.left_action_items.append(['menu', lambda x: self.toggle_nav_drawer()])

    def logout(self):
        self.ids.w_toolbar.left_action_items = []
        self.ids.screen_manager.current = 'screen_login'
        self.set_data("logged", "False")


    def navigate_to(self, page):
        self.ids.screen_manager.current = page

    def open_menu(self, *args):
        self.toggle_nav_drawer()

class Main(MDApp):
    def __init__(self, *args, **kwargs):
        MDApp.__init__(self, *args, **kwargs)
        self.theme_cls.primary_palette = "DeepOrange"


Main().run()