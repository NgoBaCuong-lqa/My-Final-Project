import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import unittest
import time
from selenium.webdriver.support.ui import Select
class product_display(unittest.TestCase):
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
        list_suggest_keywords_xpath = ('//*[@id="index"]/div[2]/ul/li')
        index = 2
        keyword_Title = self.driver.find_element_by_xpath(f'{list_suggest_keywords_xpath}[{index}]').text
        self.driver.find_element_by_xpath(f'{list_suggest_keywords_xpath}[{index}]').click()
        productTitle = self.driver.find_element_by_xpath('//*[@id="center_column"]/div/div/div[3]/h1').text
        self.assertIn(productTitle, keyword_Title, "not matching")
        time.sleep(5)
    def tearDown(cls):
        cls.driver.quit()
if __name__== '__main__':
    unittest.main()