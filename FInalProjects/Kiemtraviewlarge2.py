from selenium import webdriver
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import unittest
import time
class Chitietsanpham(unittest.TestCase):
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
        e = self.driver.find_element_by_xpath('//*[@id="bigpic"]')
        location = e.location
        size = e.size
        w, h = size['width'], size['height']
        print(location)
        print(size)
        print(w, h)

        self.driver.find_element_by_xpath('//*[@id="view_full_size"]/span').click()
        time.sleep(2)
        f = self.driver.find_element_by_xpath('//*[@id="product"]/div[2]/div')
        location = e.location
        size = f.size
        w, h = size['width'], size['height']
        print(location)
        print(size)
        print(w, h)

        if self.driver.find_element_by_xpath('//*[@id="product"]/div[2]/div'):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def tearDown(cls):
            cls.driver.quit()

if __name__== "__main__":
    unittest.main()