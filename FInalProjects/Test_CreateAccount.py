from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner

import unittest
class CreateAccount(unittest.TestCase):
    def testsignin(self):
        print("This is Login")
        self.assertTrue(True)


driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver.get("http://automationpractice.com/index.php")
driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='email_create']").send_keys("ngobacuong@gmail.com")
driver.find_element_by_xpath("//*[@id='SubmitCreate']").click()

mess = ('//*[@id="create_account_error"]')
if mess is not None:
    print ("True")
else:
    print("False")


    def tearDown(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()

time.sleep(10)