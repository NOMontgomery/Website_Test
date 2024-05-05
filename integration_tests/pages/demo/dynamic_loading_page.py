from selenium.webdriver.common.by import By
from integration_tests.pages.demo.base_demo_page import BaseDemoPage
from . import config


class DynamicLoadingPage(BaseDemoPage):
    _start_button = {"by": By.CSS_SELECTOR, "value": "#start button"}
    _finish_text = {"by": By.ID, "value": "finish"}

    def ___init___(self, driver):
        super.__init__(driver)

    def load_example(self, example_number):
        self._demo_load("/dynamic_loading/" + example_number)
        self._click(self._start_button)

    def finish_text_present(self):
        return self._is_displayed(self._finish_text, 10)
