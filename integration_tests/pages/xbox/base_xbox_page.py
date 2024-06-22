from integration_tests.pages.base_page import BasePage
from . import config


class BaseXboxPage(BasePage):
    _baseurl = config.baseurl

    def _init__(self, driver):
        super.__init__(driver)
        self.url_ = ""

    def _is_current_xbox_page(self, url):
        if url.startswith("http"):
            self.url_ = url
        else:
            self.url_ = BaseXboxPage._baseurl + url

        return self.driver.current_url in self.url_

    def _xbox_load(self, url):
        if url.startswith("http"):
            self.url_ = url
        else:
            self.url_ = BaseXboxPage._baseurl + url

        self._load(self.url_)

    def _get_text(self, locator):
        return self._find(locator).text

    def _get_attribute(self, locator):
        return self._find(locator).get_attribute("outerHTML")