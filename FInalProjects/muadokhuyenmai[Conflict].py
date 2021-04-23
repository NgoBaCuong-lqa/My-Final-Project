from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import unittest
import time
class Search3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        cls.driver.maximize_window()
        time.sleep(3)

    def test_muadokhuyenmai(self):
        self.driver.get("http://automationpractice.com/index.php")
        picture7 = self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[7]/div/div[1]/div/a[1]/img')
        actions = ActionChains(self.driver)
        actions.move_to_element(picture7).perform()
        time.sleep(2)

        self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[7]/div/div[2]/div[1]/span[3]').text




