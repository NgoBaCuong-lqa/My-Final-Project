from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.webdriver.support.ui import Select
class Search2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox(executable_path=r"C:\FireFox\geckodriver.exe")
        cls.driver.get("http://automationpractice.com/index.php")
        cls.driver.maximize_window()
        time.sleep(3)
    def test_element(self):
        self.driver.find_element_by_xpath('//*[@id="search_query_top"]').click()
        self.driver.find_element_by_xpath('//*[@id="search_query_top"]').send_keys("Dress")
        time.sleep(5)
        #if (self.driver.find_element_by_class_name('search_query')).text == "Dress":
            #print ("True")
        #else:
            #print("False")

        lst = self.driver.find_elements_by_xpath('//*[@id="index"]/div[2]/ul/li')
        for elm in lst:
            elm_text = elm.text
            self.assertIn("Dress", elm_text, 'False')
    def tearDown(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()
