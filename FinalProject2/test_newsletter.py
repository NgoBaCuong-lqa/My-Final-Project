from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from parameterized import parameterized
class newletter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\FireFox\geckodriver.exe")
        self.driver.maximize_window()
        time.sleep(3)

    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_sendtofriend(self, browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome(executable_path=r"C:\Driver\chromedriver.exe")
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"C:\FireFox\geckodriver.exe")
            time.sleep(3)
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//*[@id='newsletter-input']").send_keys("buiquanghiep@gmail.com")
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

