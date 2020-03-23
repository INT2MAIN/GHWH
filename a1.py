import unittest

from windows import get_new_window
import unittest
from selenium import webdriver
import  time as t
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome()
        t.sleep(2)
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
    def test_something(self):

        driver=self.driver
        driver.get('E:\Study\GHWH\gh.html')
        t.sleep(6)
        driver.find_element_by_id('aa').click()
        t.sleep(3)
        #get_new_window(driver)
        t.sleep(2)
        driver.get_screenshot_as_file("E:\Study\GHWH\est.png")
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
