import pytest
from selenium.webdriver.common.by import By
from integration_tests.pages.xbox.xbox_home_page import XboxHomePage
from selenium.webdriver.common.keys import Keys


class TestXboxHomePage:
    # test_data
    search_icon = {"by": By.CSS_SELECTOR, "value": "#search"}
    search_bar = {"by": By.CSS_SELECTOR, "value": "#cli_shellHeaderSearchInput"}
    dm5 = "https://www.xbox.com/en-us/Search/Results?q=Devil+may+5"
    dm5_text = '<span class="ProductCard-module__title___nHGIp typography-module__xdsBody2___RNdGY">Devil May Cry 5</span>'
    dm5_path_confirm_text = '//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/section/div/ol/li[1]/div/a/div[2]/span[1]'
    dm5_confirm_text = {"by": By.XPATH, "value": dm5_path_confirm_text}
    dm5_path_select = '//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/section/div/ol/li[1]/div/a/div[1]/img'
    dm5_select = {"by": By.XPATH, "value": dm5_path_select}
    # confirm_dm5_buy_text_path = '/html/body/div[1]/div/div/div[3]/div/div[1]/div[1]/div[6]/div/div[1]/button'
    confirm_dm5_buy_text = {"by": By.XPATH, "value": '/html/body/div[1]/div/div/div[3]/div/div[1]/div[1]/div[6]/div/div[1]/div[1]/div/ul/li[1]/a/div/div[1]'}

    @pytest.fixture
    def xbox_home_page(self, driver):
        return XboxHomePage(driver)

    def test_xbox_home_page(self, xbox_home_page):
        xbox_home_page._xbox_load("/")
        xbox_home_page._wait_for_page_to_load(10)
        assert xbox_home_page._is_current_xbox_page("/")

    def test_search_bar_button(self, xbox_home_page):
        xbox_home_page._xbox_load("/")
        xbox_home_page._wait_for_page_to_load(10)
        search = xbox_home_page._find(self.search_icon)
        xbox_home_page._click_blocked_element(search)
        # search_text = xbox_home_page._find(self.search_bar)
        xbox_home_page._type(self.search_bar, "Devil May Cry 5")
        xbox_home_page._type(self.search_bar, Keys.ENTER)
        assert xbox_home_page._get_text(self.dm5_confirm_text) == "Devil May Cry 5"

    def test_dm5_select(self, xbox_home_page):
        xbox_home_page._xbox_load("/Search/Results?q=devil+may+cry+5")
        xbox_home_page._wait_for_page_to_load(10)
        # select_dm5 = xbox_home_page._find(self.dm5_select)
        xbox_home_page._click(self.dm5_select)
        click_buy = select_dm5 = xbox_home_page._find(self.confirm_dm5_buy_text)
        xbox_home_page._click_blocked_element(click_buy)
        print(f'outer text \n')
        # assert xbox_home_page._get_attribute(self.confirm_dm5_buy_text)
