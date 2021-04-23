from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
import unittest
import time
class kiemtra_viewlarge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        cls.driver.maximize_window()
        time.sleep(3)

    def test_chitietsanpham(self):
        self.driver.get("http://automationpractice.com/index.php")
        picture7 = self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[4]/div/div[1]/div/a[1]/img')
        actions = ActionChains(self.driver)
        actions.move_to_element(picture7).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[4]/div/div[1]/div/a[1]/img').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="bigpic"]').click()
    def tearDown(cls):
        cls.driver.quit()
if __name__== "__main__":
    unittest.main()
