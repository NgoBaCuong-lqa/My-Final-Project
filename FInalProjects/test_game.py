from selenium import webdriver
import unittest
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()


class test_game(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_sendtofriend(self):
        # tìm sản phẩm và click()
        time.sleep(4)
        self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[2]/div/div[1]/div/a[1]/img').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="send_friend_button"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="friend_name"]').send_keys("ngobacuong")
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="friend_email"]').send_keys("oknha@gmail.com")
        time.sleep(4)
        self.driver.find_element_by_xpath('//*[@id="sendEmail"]').click()
        time.sleep(10)
    def tearDown(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()
