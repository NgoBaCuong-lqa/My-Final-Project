from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import unittest
import time
from selenium.webdriver.support.ui import Select
class Search3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get("http://automationpractice.com/index.php")
        cls.driver.maximize_window()
        time.sleep(3)
    def test_element(self):
        self.driver.find_element_by_xpath('//*[@id="search_query_top"]').click()
        self.driver.find_element_by_xpath('//*[@id="search_query_top"]').send_keys("Dress")
        self.driver.find_element_by_name('submit_search').click()
        time.sleep(5)
        product=self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[2]/div[1]/span[1]').text

        self.assertNotEqual(' ', product, "fail" )

    def tearDown(cls):
        cls.driver.quit()
if __name__== '__main__':
    unittest.main()
