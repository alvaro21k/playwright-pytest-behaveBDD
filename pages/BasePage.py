from utilities import configReader
import logging
import allure

from utilities.LogUtil import Logger

log = Logger(__name__,logging.INFO)

class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self,locator):
        with allure.step(f"Clicking on an element {locator}"):
            self.page.locator(configReader.readConfig("locators",locator)).click()
            log.logger.info(f"Clicking on an element {locator}")

    def type(self, locator, value):
        with allure.step(f"Typing {value} on an element {locator}"):
            self.page.locator(configReader.readConfig("locators", locator)).fill(value)
            log.logger.info(f"Typing {value} in an element {locator}")

    def move_to(self,locator):
        with allure.step(f"Moving to an element {locator}"):
            self.page.locator(configReader.readConfig("locators",locator)).hover()
            log.logger.info(f"Moving to an element {locator}")