from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import chromedriver_autoinstaller
import HtmlTestRunner

class create_success(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def testcreateaccount(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]').click()
        time.sleep(3)
        self.driver.find_element_by_id('email_create').send_keys("ngobacuong1008@gmail.com")
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="SubmitCreate"]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="customer_firstname"]').send_keys("huy")
        self.driver.find_element_by_xpath('//*[@id="customer_lastname"]').send_keys("dung")
        # driver.find_element_by_xpath('//*[@id="email"]').send_keys("nguyenquanghuy@gmail.com")
        self.driver.find_element_by_xpath('//*[@id="passwd"]').send_keys("123456")
        self.driver.find_element_by_id("address1").send_keys("số 3,Cầu giấy,Hà Nội")
        self.driver.find_element_by_id("city").send_keys("LQA")
        element = self.driver.find_element_by_id("id_state")
        drp = Select(element)
        drp.select_by_visible_text("Alabama")
        self.driver.find_element_by_xpath('//*[@id="postcode"]').send_keys("10000")
        self.driver.find_element_by_xpath('//*[@id="phone_mobile"]').send_keys("0326839977")
        self.driver.find_element_by_id('submitAccount').click()
        time.sleep(5)
        title = self.driver.title
        self.assertEqual("My account - My Store", title, "webpage title is not matching")


        time.sleep(10)
if __name__ == '__main__':
    unittest.main()
