from selenium.webdriver.common.by import By
from integration_tests.pages.base_page import BasePage


class BestBuyHomePage(BasePage):
    _some_element = {"by": By.ID, "value": ""}


    def ___init___(self, driver):
        self.driver = driver

    
