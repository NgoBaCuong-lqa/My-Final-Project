from selenium import webdriver
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import unittest
import time
class sendtofriend(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.maximize_window()
        time.sleep(3)

    def test_sharetotwiter(self):
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('nguyenhuydung14568@gmail.com')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('123456')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="SubmitLogin"]').click()
        time.sleep(3)
        self.driver.get('http://automationpractice.com/')
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[2]/div/div[1]/div').click()
        time.sleep(2)
    def tearDown(cls):
        cls.driver.quit()
if __name__== "__main__":
    unittest.main()

