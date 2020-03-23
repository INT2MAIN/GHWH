import unittest
from time import *

from selenium import webdriver
from selenium.webdriver.common.by import By

import jietu


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://home.ydyksoft.cn:8090/webhis/')
    def tearDown(self):
        self.driver.quit()
    def test_login(self):
        '''注释'''
        role_path = '//div[@class="rolelist"]/ul/li[3]'
        self.driver.find_element_by_name('username').send_keys("ZJB")
        # password
        self.driver.find_element_by_name('password').send_keys("797636")
        # role_name
        self.driver.find_element_by_id('role_name').click()
        sleep(1)
        self.driver.find_element_by_xpath(role_path).click()
        sleep(1)
        # login
        #self.driver.find_element_by_id('login').click()

        #self.assertEqual(1, 2, msg='这是错误')
        try:
            self.assertEqual(1,2,msg='这是错误')
        except Exception as e:
            jietu.getImage(self.driver)
            #self.driver.get_screenshot_as_base64()
        raise
        sleep(1)
        # self.assertEqual(case, actul_case)
if __name__ == '__main__':
    unittest.main()
