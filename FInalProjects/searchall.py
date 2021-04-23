import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import unittest
import time
from selenium.webdriver.support.ui import Select
class searchall(unittest.TestCase):
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
    def check_element(self):
        product = self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[2]').text
        list = product.split()# tách các phần tử trong 7 results have been found
        quantity = int(list[0])#số lượng

        x = self.driver.find_elements_by_xpath('//*[@id="center_column"]/ul/li') #tim dduowc tat ca cac san pham
        quantity_product = len(x) #số lượng

        self.assertEqual(quantity, quantity_product, "Fail!")

    def tearDown(cls):
        cls.driver.quit()

if __name__== '__main__':
    unittest.main()