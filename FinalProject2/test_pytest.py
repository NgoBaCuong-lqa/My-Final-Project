import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys


@pytest.mark.usefixtures("driver_init_2")
class BasicTest:
    pass


class Test_URL_Firefox(BasicTest):
    def test_google_search(self):
        self.driver.get('https://www.google.com/')
        self.driver.maximize_window()
        title = "Google"
        assert title == self.driver.title

        search_text = "LambdaTest"
        search_box = self.driver.find_element_by_xpath("//input[@name='q']")
        search_box.send_keys(search_text)

        time.sleep(5)

        # Option 1 - To Submit the search
        # search_box.submit()

        # Option 2 - To Submit the search
        search_box.send_keys(Keys.ARROW_DOWN)
        search_box.send_keys(Keys.ARROW_UP)
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)

        time.sleep(5)

        # Click on the LambdaTest HomePage Link
        title = "Cross Browser Testing Tools | Free Automated Website Testing | LambdaTest"
        lt_link = self.driver.find_element_by_xpath(
            "//h3[.='LambdaTest: Cross Browser Testing Tools | Free Automated ...']")
        lt_link.click()

        time.sleep(10)
        assert title == self.driver.title
        time.sleep(2)

    def test_lambdatest_blog_load(self):
        self.driver.get('https://www.lambdatest.com/blog/')
        self.driver.maximize_window()

        expected_title = "LambdaTest | A Cross Browser Testing Blog"
        assert expected_title == self.driver.title
        time.sleep(5)