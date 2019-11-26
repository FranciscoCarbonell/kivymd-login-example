from pages.base import BaseScreen
from kivy.properties import ObjectProperty

class PageLogin(BaseScreen):
    email = ObjectProperty()
    password = ObjectProperty()

    def loggin_user(self):
        if self.email.text == 'admin' and self.password.text == 'admin':
            self.root.navigate_to("screen_inicio")
            self.enable_nav()
            self.root.set_data("logged", "True")

    def enable_nav(self):
        menu = ["menu", self.root.open_menu]
        self.root.ids.w_toolbar.left_action_items.append(menu)