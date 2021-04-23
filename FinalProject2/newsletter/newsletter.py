from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
class Newsletter(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox(executable_path="C:\Driver\geckodriver.exe")
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()
    def test_01(self):
        self.driver.find_element_by_xpath("//*[@id='newsletter-input']").send_keys("buibaochau444@gmail.com")
        self.driver.find_element_by_xpath("//*[@id='newsletter_block_left']/div/form/div/button").click()

        time.sleep(10)

        # (' Newsletter : You have successfully subscribed to this newsletter.')
        if self.driver.find_element_by_xpath('//*[@id="columns"]/p'):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def tearDown(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()

