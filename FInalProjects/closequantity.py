from selenium import webdriver
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import unittest
import time
class close_quantity(unittest.TestCase):
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
        time.sleep(2)
        self.driver.find_element_by_id('quantity_wanted').clear()
        self.driver.find_element_by_xpath('//*[@id="quantity_wanted"]').send_keys(0)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="quantity_wanted"]').clear()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="quantity_wanted"]').send_keys(1)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="add_to_cart"]/button').click()
        time.sleep(3)
        successfulproduct = self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[1]/h2').text
        time.sleep(3)
        self.assertEqual('Product successfully added to your shopping cart', successfulproduct, "not find product")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[1]/span').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div/div[3]/div/a').click()

        if self.driver.find_element_by_xpath('//*[@id="product_4_16_0_0"]/td[1]/a/img'):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def tearDown(cls):
        cls.driver.quit()

if __name__== "__main":
    unittest.main()
