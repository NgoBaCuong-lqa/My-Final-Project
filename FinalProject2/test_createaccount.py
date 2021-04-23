from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.support.ui import Select
from parameterized import parameterized
class test_paralel(unittest.TestCase):
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
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a').click()
        time.sleep(3)
        self.driver.find_element_by_id('email_create').send_keys("daobaloc@gmail.com")
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="SubmitCreate"]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="customer_firstname"]').send_keys("cuong")
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
        time.sleep(3)

    def tearDown(cls):
        cls.driver.quit()

        time.sleep(10)
if __name__ == '__main__':
    unittest.main()
