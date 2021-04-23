from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import unittest
import time
from selenium.webdriver.support.ui import Select
class Search(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get("http://automationpractice.com/index.php")
        cls.driver.maximize_window()
        time.sleep(3)
    def test_element(self):
        self.driver.find_element_by_xpath('//*[@id="search_query_top"]').click()
        self.driver.find_element_by_xpath('//*[@id="search_query_top"]').send_keys("Dress")
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="search_query_top"]').clear()
        time.sleep(5)

    def test_search(self):
        print("Search")
        self.assertTrue(True)
    def tearDown(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()
