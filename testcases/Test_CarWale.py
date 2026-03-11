import time

import pytest

from pages.HomePage import HomePage
from pages.NewCarsPage import NewCarsPage
from testcases.BaseTest import BaseTest
from utilities import dataProvider
import allure

class Test_CarWale(BaseTest):

    @allure.feature("Find New Cars Test")
    @allure.severity(allure.severity_level.MINOR)
    def test_finding_new_cars(self, page):
        with allure.step("*****Executing Finding New Cars Test*****"):
            home = HomePage(page)
            home.find_new_cars()
            time.sleep(3)

    @allure.feature("Select Cars Test")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("carBrand",dataProvider.get_data("NewCarsTest"))
    def test_select_cars(self, page, carBrand):
        with allure.step("*****Executing Finding New Cars Test*****"):
            home = HomePage(page)

            if carBrand == "BMW":
                home.find_new_cars().go_to_BMW()
            elif carBrand == "MG":
                home.find_new_cars().go_to_MG()
            elif carBrand == "Toyota":
                home.find_new_cars().go_to_toyota()
            elif carBrand == "Honda":
                home.find_new_cars().go_to_honda()

            time.sleep(3)
