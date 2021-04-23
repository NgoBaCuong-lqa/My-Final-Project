from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import unittest
import time
from selenium.webdriver.support.ui import Select
class Search(unittest.TestCase):
    @classmethod
    def test_upper(self):
        self.assertEqual('love'.upper(), 'LOVE')

if __name__ == '__main__':
    unittest.main()
