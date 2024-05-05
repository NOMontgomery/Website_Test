import pytest
from selenium.webdriver.common.by import By
from ..pages.xbox_home_page import XboxHomePage
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class TestXboxHomePage:
    search_icon = {"by": By.CSS_SELECTOR, "value": "#search"}
    search_bar = {"by": By.CSS_SELECTOR, "value": "#cli_shellHeaderSearchInput"}

    @pytest.fixture
    def xbox_home_page(self, driver):
        return XboxHomePage(driver)

    def test_xbox_home_page(self, xbox_home_page):
        xbox_home_page.headless_false()
        xbox_home_page._load("")
        xbox_home_page._wait_for_page_to_load(10)
        search = xbox_home_page._find(self.search_icon)
        xbox_home_page._click_blocked_element(search)


        # assert xbox_home_page._is_current_page()
