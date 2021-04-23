from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import unittest
import time
class successfulbuy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        cls.driver.maximize_window()
        time.sleep(3)

    def test_step_buy(self):
        self.driver.get("http://automationpractice.com/index.php")
        picture=self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[1]/img')
        addtocard=self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[2]/div/div[2]/div[2]/a[1]')
        continueshopping=self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span')

        actions=ActionChains(self.driver)
        actions.move_to_element(picture).perform()
        self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span').click()
        time.sleep(2)


        picture2=self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[6]/div/div[1]/div/a[1]/img')
        actions=ActionChains(self.driver)
        actions.move_to_element(picture2).perform()
        self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[6]/div/div[2]/div[2]/a[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span').click()
        time.sleep(2)

        picture3=self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[7]/div/div[1]/div/a[1]/img')
        actions=ActionChains(self.driver)
        actions.move_to_element(picture3).perform()
        self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[7]/div/div[2]/div[2]/a[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a').click()
        time.sleep(3)
        total = self.driver.find_element_by_xpath('//*[@id="total_product"]').text
        x= list = float(total[1:])
        print(list)

        y= lst = [16.51, 30.50, 16.40]
        print(sum(lst))

        self.driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('nguyenhuydung14568@gmail.com')
        self.driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('123456')
        self.driver.find_element_by_id('SubmitLogin').click()
        self.driver.find_element_by_name('processAddress').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="cgv"]').click()
        time.sleep(3)
        self.driver.find_element_by_name('processCarrier').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="HOOK_PAYMENT"]/div[2]/div/p').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="cart_navigation"]/button').click()
        time.sleep(1)


    def tearDown(cls):
        cls.driver.quit()


if __name__== "__main__":
    unittest.main()