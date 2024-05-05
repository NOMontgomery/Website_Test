from integration_tests.pages.base_page import BasePage
from . import config


class BaseDemoPage(BasePage):
   
    _baseurl = config.baseurl

    def _init__(self, driver):
        super.__init__(driver)
        self.url_ = ""

    def _demo_load(self, url):
        if url.startswith("http"):
            self.url_ = url
        else:
            self.url_ = BaseDemoPage._baseurl + url

        self._load(self.url_)
       

