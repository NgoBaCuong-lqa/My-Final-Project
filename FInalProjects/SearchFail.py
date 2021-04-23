import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import unittest
import time
from selenium.webdriver.support.ui import Select
class search_fail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get("http://automationpractice.com/index.php")
        cls.driver.maximize_window()
        time.sleep(3)
    def test_element(self):
        self.driver.find_element_by_xpath('//*[@id="search_query_top"]').click()
        keyword = "dressSSSss"
        self.driver.find_element_by_xpath('//*[@id="search_query_top"]').send_keys(keyword)
        self.driver.find_element_by_name('submit_search').click()
        message=self.driver.find_element_by_xpath('//*[@id="center_column"]/p').text
        self.assertEqual(f'No results were found for your search "{keyword}"',message, "Fail")
    def tearDown(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()
