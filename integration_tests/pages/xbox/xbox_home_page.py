import pytest
from selenium import webdriver
from integration_tests.pages.base_page import BasePage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from integration_tests.tests import config
from integration_tests.common.driver_manager import DriverManager
from .base_xbox_page import BaseXboxPage


class XboxHomePage(BaseXboxPage):
    # search_icon = {"by": By.CSS_SELECTOR, "value": "#search"}

    # search_bar = {"by": By.CSS_SELECTOR, "value": "#cli_shellHeaderSearchInput"} dm5_path = '//*[
    # @id="PageContent"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/section/div/ol/li[1]/div/a/div[1]/img' dm5 = {
    # "by": By.XPATH, "value": dm5_path} dm5_buy_path = '#PageContent > div > div:nth-child(1) >
    # div.ModuleContainer-module__container___pkhPl.ProductDetailsHeader-module__container___zvKSX >
    # div.FadeContainers-module__fadeIn___5xlsD.FadeContainers-module__widthInherit___5fuOa > div > div > button')
    # dm5_buy = {"by": By.CSS_SELECTOR, "value": dm5_buy_path}

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._page_loaded_indicator = (By.ID, "c-uhff-footer_aboutourads")

    # def headless_false(self):
    #     return config.headless == ()
    #
    # #
    # @pytest.fixture
    # def search(self, icon):
    #     # I want to use search_icon to click on the search bar then start typing
    #     self._find(self.search_icon)
    #     #I need it to click on the search input bar
    #     # self._find(self.search_bar)
