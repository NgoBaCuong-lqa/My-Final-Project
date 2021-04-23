from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.webdriver.support.ui import Select
class contactUs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox(executable_path=r"C:\FireFox\geckodriver.exe")

        cls.driver.maximize_window()
        time.sleep(3)
    def test_element(self):
        self.driver.get("http://automationpractice.com/index.php")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='contact-link']/a").click()
        time.sleep(2)
        elt = self.driver.find_element_by_id("id_contact")
        self.drp = Select(elt)
        self.drp.select_by_value("2")
        self.driver.find_element_by_id('email').send_keys("nguyenhuydung14568@gmail.com")
        time.sleep(2)
        elm = self.driver.find_element_by_id("fileUpload")
        elm.send_keys(r"C:\Users\lqa\Desktop\XPATH.txt")
        self.driver.find_element_by_id('message').send_keys("123456")
        time.sleep(2)
        self.driver.find_element_by_id('submitMessage').click()
        time.sleep(10)
        if self.driver.find_element_by_xpath("/html/head/title"):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def tearDown(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()
