import unittest
import HtmlTestRunner
from Newslttter.Newsletter import Newsletter
from Newslttter.quantity1 import Chitietsanpham
from Search2 import Search2
from TestSearchOnce import Search
from test_writeacomment import writeacomment
from Test_successbuy import successfulbuy
from test_sharetotwiter import sharetotwiter
from test_sendtofriend import sendtofriend
from Test_CreateAccount import CreateAccount
from SearchFail import search_fail
from Quantity import quantity
from test_productdisplay import product_display
from test_game import test_game
from searchall import searchall
from change_buy import change_buy
from closequantity import close_quantity
from contactUs import contactUs
from createsucessaccount import create_success
from kiemtra_viewlarge import kiemtra_viewlarge
from muadokhuyenmai import muadokhuyenmai


tc1=unittest.TestLoader().loadTestsFromTestCase(Newsletter)
tc2=unittest.TestLoader().loadTestsFromTestCase(Chitietsanpham)
tc3=unittest.TestLoader().loadTestsFromTestCase(Search2)
tc4=unittest.TestLoader().loadTestsFromTestCase(Search)
tc5=unittest.TestLoader().loadTestsFromTestCase(writeacomment)
tc6=unittest.TestLoader().loadTestsFromTestCase(successfulbuy)
tc7=unittest.TestLoader().loadTestsFromTestCase(sharetotwiter)
tc8=unittest.TestLoader().loadTestsFromTestCase(sendtofriend)
tc9=unittest.TestLoader().loadTestsFromTestCase(CreateAccount)
tc10=unittest.TestLoader().loadTestsFromTestCase(search_fail)
tc11=unittest.TestLoader().loadTestsFromTestCase(quantity)
tc12=unittest.TestLoader().loadTestsFromTestCase(product_display)
tc13=unittest.TestLoader().loadTestsFromTestCase(test_game)
tc14=unittest.TestLoader().loadTestsFromTestCase(searchall)
tc15=unittest.TestLoader().loadTestsFromTestCase(change_buy)
tc16=unittest.TestLoader().loadTestsFromTestCase(close_quantity)
tc17=unittest.TestLoader().loadTestsFromTestCase(contactUs)
tc18=unittest.TestLoader().loadTestsFromTestCase(CreateAccount)
tc19=unittest.TestLoader().loadTestsFromTestCase(kiemtra_viewlarge)
tc20=unittest.TestLoader().loadTestsFromTestCase(muadokhuyenmai)
tc21=unittest.TestLoader().loadTestsFromTestCase(create_success)


sanityTestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4,tc5,tc6,tc7,tc8,tc9,tc10,tc11,tc12,tc13,tc14,tc15,tc16,tc17,tc18,tc19,tc20,tc21])


unittest.TextTestRunner().run(sanityTestSuite)
if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\lqa\PycharmProjects\FInalProjects\Reportsall',combine_reports=True,report_name="Test Report"))
