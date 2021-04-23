from selenium import webdriver
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import unittest
import time
import driver
class sharetotwiter(unittest.TestCase):
    def setUp(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        time.sleep(3)

    def test_sharetotwiter(self):
        self.driver.get("http://automationpractice.com/index.php")
        picture1 = self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[1]/img')
        actions = ActionChains(self.driver)
        actions.move_to_element(picture1).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[1]/img').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="center_column"]/div/div/div[3]/p[7]/button[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="center_column"]/div/div/div[3]/p[7]/button[1]').click()
        time.sleep(3)
        #chuyển trang
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys("ngobacuong2016@gmail.com")
        time.sleep(10)
        #self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[2]/label/div/div[1]').send_keys("nguyenduycuong@gmail.com")
        #time.sleep(10)
        #self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/span/span/span').click()
        #time.sleep(3)

    def tearDown(cls):
            cls.driver.quit()
if __name__ == "__main":
    unittest.main()
