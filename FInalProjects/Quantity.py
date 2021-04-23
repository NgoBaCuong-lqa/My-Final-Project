from selenium import webdriver
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import unittest
import time
class quantity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        cls.driver.maximize_window()
        time.sleep(3)

    def test_chitietsanpham(self):
        self.driver.get("http://automationpractice.com/index.php")
        picture4 = self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[4]/div/div[1]/div/a[1]/img')
        actions = ActionChains(self.driver)
        actions.move_to_element(picture4).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[4]/div/div[1]/div/a[1]/img').click()
        time.sleep(2)
        self.driver.find_element_by_id('quantity_wanted').click()
        time.sleep(1)
        self.driver.find_element_by_id('quantity_wanted').clear()
        self.driver.find_element_by_xpath('//*[@id="quantity_wanted"]').send_keys(0)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="add_to_cart"]/button/span').click()
        time.sleep(2)
        x =self.driver.find_element_by_xpath('//p[@class = "fancybox-error"]').text
        self.assertEqual('Null quantity.', x, "not find")
    def tearDown(cls):
        cls.driver.quit()
if __name__== "__main__":
    unittest.main()