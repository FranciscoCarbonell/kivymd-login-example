from pages.base import BaseScreen

class PageMain(BaseScreen):
    def logout(self, *args):
        self.root.logout()