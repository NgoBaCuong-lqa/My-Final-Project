import unittest
import HtmlTestRunner

from comtact.ContacUs import contactUs
from newsletter.newsletter import newletter
from test.test_writeacomment import writeacomment
from test.test_sendtofriend import sendtofriend
from test.test_createsuccessaccount import create_success

tc1=unittest.TestLoader().loadTestsFromTestCase(contactUs)
tc2=unittest.TestLoader().loadTestsFromTestCase(newletter)
tc3=unittest.TestLoader().loadTestsFromTestCase(writeacomment)
tc4=unittest.TestLoader().loadTestsFromTestCase(sendtofriend)
tc5=unittest.TestLoader().loadTestsFromTestCase(create_success)



sanityTestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4,tc5])


unittest.TextTestRunner().run(sanityTestSuite)
if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\lqa\PycharmProjects\FinalProject2\Reportsall',combine_reports=True,report_name="Test Report"))
