import time

from pages.HomePage import HomePage
from testcases.BaseTest import BaseTest
import allure

class Test_CarWale(BaseTest):

    @allure.feature("Find New Cars Test")
    @allure.severity(allure.severity_level.MINOR)
    def test_finding_new_cars(self, page):
        with allure.step("*****Executing Finding New Cars Test*****"):
            home = HomePage(page)
            home.find_new_cars()
