from time import sleep

from selenium.webdriver import ActionChains

from windows import get_new_window
import unittest
from selenium import webdriver
import  time as t
class MyTestCase(unittest.TestCase):
    '''这是一个百度用例集'''
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome()
        t.sleep(2)
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
    def setUp(self):
        self.driver.get('http://home.ydyksoft.cn:8090/webhis/')

        t.sleep(2)
    def tearDown(self):
        print('这是一条用例')

    def test_ghwh(driver):
        get_new_window(driver)
        driver.find_element_by_link_text('挂号管理').click()
        driver.find_element_by_link_text('挂号管理').click()
        sleep(2)
        driver.find_element_by_link_text('挂号维护').click()
        get_new_window(driver)
        sleep(2)
        ghwh = driver.switch_to.frame(1)
        # driver.switch_to.frame('baidu)
        ghwh_mzh = driver.find_element_by_id('CMZH')
        actions = ActionChains(driver)
        actions.move_to_element(ghwh_mzh)
        actions.double_click()
        actions.perform()
        sleep(3)
        driver.switch_to.default_content()
        mzh_frame = driver.find_element_by_xpath('//*[@id="layui-layer-iframe2"]')
        driver.switch_to.frame(mzh_frame)
        # filter--挂号维护-门诊号
        sleep(2)
        driver.find_element_by_id('filter').send_keys('2001000062')
        sleep(3)
        # 检索门诊号按钮
        driver.find_element_by_xpath('//*[@id="query_btn"]').click()
        sleep(1)
        driver.switch_to.default_content()
        sleep(2)
        # 点击确定门诊号按钮
        driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]').click()