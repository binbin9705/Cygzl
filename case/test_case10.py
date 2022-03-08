import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PublicMethod import WebGetDemo
from selenium.webdriver.common.by import By
import warnings
import random


# @unittest.skip('调试')
class Test10(unittest.TestCase):
    '''开放发展'''

    @classmethod
    def setUpClass(cls):
        # 启动浏览并设置相关选项
        cls.driver = webdriver.Chrome(options=WebGetDemo.Runmian(cls).options())
        cls.imgs = []
        WebGetDemo.Runmian(cls.driver).open('http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard')
        WebGetDemo.Runmian(cls.driver).login('ihqd-test', 'ihqd-test@6688')
        # 消除警告
        warnings.simplefilter('ignore', ResourceWarning)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    def setUp(self):
        # # 启动浏览并设置相关选项
        # self.driver = webdriver.Chrome(options=WebGetDemo.Runmian(self).options())
        # self.imgs = []
        # WebGetDemo.Runmian(self.driver).open('http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard')
        # WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        self.driver.refresh()
        self.driver.implicitly_wait(5)

    def add_img(self):
        # 1、下面注释掉的这行代码作用是不管用例是否执行成功，只要在执行过程加了self.add_img()操作，那么最后生成的报告中含有该执行过程的截图，如果不添加则默认对用例失败进行截图
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def tearDown(self):
        # WebGetDemo.Runmian(self.driver).quit()
        pass
    def test_01(self):
        '''开放发展-结构分析-随机切换企业数量统计条件'''
        try:
            time.sleep(3)
            # 点击开放发展
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[3]/li/div/i')
            time.sleep(3)
            # 点击结构分析
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(3)
            # 点击企业数量统计下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/div[1]/div/span/span/i')
            time.sleep(3)
            # 随机选择一种统计类型.
            num = random.randint(3, 4)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择类型的class
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_02(self):
        '''开放发展-结构分析-随机切换币种统计条件'''
        try:
            # time.sleep(3)
            # # 点击开放发展
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[3]/li/div/i')
            # time.sleep(3)
            # # 点击结构分析
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(3)
            # 点击币种下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/span/span/button/span/i')
            time.sleep(3)
            # 随机选择一种统计类型.
            num = random.randint(1, 9)
            js = 'document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择类型的class
            js2 = 'return document.getElementsByClassName("el-checkbox__input")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('is-checked', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_03(self):
        '''开放发展-结构分析-随机选择地区'''
        try:
            # time.sleep(3)
            # # 点击开放发展
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[3]/li/div/i')
            # time.sleep(3)
            # # 点击结构分析
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(3)
            # 点击地区下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="tipMulM"]/button/span/i')
            time.sleep(3)
            # 清空地区后随机选择一个
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="tipMulM"]/div/div/div[2]/div/div[2]/button[1]/span')
            time.sleep(2)
            # 随机选择一个地区.
            num = random.randint(10, 43)
            js = 'document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择地区的class
            js2 = 'return document.getElementsByClassName("el-checkbox__input")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            js3 = 'return document.getElementsByClassName("el-checkbox__original")[' + str(
                num) + '].getAttribute("value")'
            textvalue = self.driver.execute_script(js3)
            js4 = 'return document.getElementsByClassName("selectM")[5].innerText'
            yxtext = self.driver.execute_script(js4)
            yxtext = yxtext.rstrip()
            self.assertIn('is-checked', classvalue, '用例执行失败')
            self.assertIn(yxtext, textvalue, '用例执行失败')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="tipMulM"]/div/div/div[2]/div/div[2]/button[2]/span')
            time.sleep(2)
        except Exception:
            self.add_img()
            raise

    def test_04(self):
        '''开放发展-结构分析-随机选择行业'''
        try:
            # time.sleep(3)
            # # 点击开放发展
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[3]/li/div/i')
            # time.sleep(3)
            # # 点击结构分析
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(3)
            # 点击行业选择框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/div[3]/button/span/i')
            time.sleep(3)
            # 随机选择一个点击确定
            num = random.randint(10, 29)
            js = 'document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            # 获取点击行业的class
            js2 = 'return document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('is-checked', classvalue, '用例执行失败')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/div[3]/div/div/div[3]/div/button/span')
            time.sleep(2)
        except Exception:
            self.add_img()
            raise

    def test_05(self):
        '''开放发展-结构分析-随机选择产业'''
        try:
            # time.sleep(3)
            # # 点击开放发展
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[3]/li/div/i')
            # time.sleep(3)
            # # 点击结构分析
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(3)
            # 点击产业选择框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/div[4]/button/span/i')
            time.sleep(3)
            # 随机选择一个点击确定
            num = random.randint(10, 21)
            js = 'document.getElementsByClassName("el-checkbox__inner")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            # 获取点击行业的class
            js2 = 'return document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('is-checked', classvalue, '用例执行失败')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/div[4]/div/div/div[3]/div/button/span')
            time.sleep(2)
        except Exception:
            self.add_img()
            raise

    def test_06(self):
        '''开放发展-结构分析-区域占比切换行业占比'''
        try:
            # time.sleep(3)
            # # 点击开放发展
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[3]/li/div/i')
            # time.sleep(3)
            # # 点击结构分析
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="jgfn_box_m"]/div[2]/div[1]/div[1]/span/span/i')
            time.sleep(2)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[4].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[4].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_07(self):
        '''开放发展-地域分析-随机切换币种'''
        try:
            time.sleep(3)
            # 点击开放发展
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[3]/li/div/i')
            time.sleep(3)
            # 点击地域分析
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(3)
            # 点击币种下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/span/span/button/span/i')
            time.sleep(2)
            # 随机选择一种币种
            num = random.randint(2, 9)
            js = 'document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            js2 = 'return document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('is-checked', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
