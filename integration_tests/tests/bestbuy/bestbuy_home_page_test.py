import pytest

import os

from integration_tests.pages.bestbuy.bestbuy_home_page import BestBuyHomePage


# @pytest.mark.deep
class TestBestBuyHomePage():

    @pytest.fixture
    def bestbuy_home_page(self, driver):
        return BestBuyHomePage(driver)
    
    def test_bestbuy_home_page(self, bestbuy_home_page):
        bestbuy_home_page._load("")
        assert(bestbuy_home_page._is_current_page())

