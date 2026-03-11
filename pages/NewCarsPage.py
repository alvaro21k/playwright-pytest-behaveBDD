from pages.BMWCarsPage import BMWPage
from pages.BasePage import BasePage
from pages.HondaCarsPage import HondaPage
from pages.MGCarsPage import MGPage
from pages.ToyotaCarsPage import ToyotaPage


class NewCarsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def go_to_toyota(self):
        self.click("Toyota_XPATH")

        return ToyotaPage(self.page)

    def go_to_BMW(self):
        self.click("BMW_XPATH")

        return BMWPage(self.page)

    def go_to_honda(self):
        self.click("Honda_XPATH")

        return HondaPage(self.page)

    def go_to_MG(self):
        self.click("MG_XPATH")

        return MGPage(self.page)