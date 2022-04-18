import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PublicMethod import WebGetDemo
from selenium.webdriver.common.by import By
import warnings
import random


# @unittest.skip('调试')
class Test07(unittest.TestCase):
    '''创新发展'''

    @classmethod
    def setUpClass(cls):
        # 启动浏览并设置相关选项
        cls.driver = webdriver.Chrome(options=WebGetDemo.Runmian(cls).options())
        # cls.imgs = []
        WebGetDemo.Runmian(cls.driver).open('http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard')
        WebGetDemo.Runmian(cls.driver).login(username='ihqd-test', password='ihqd-test@6688')
        # 消除警告
        warnings.simplefilter('ignore', ResourceWarning)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    def setUp(self):
        # # 启动浏览并设置相关选项
        # self.driver = webdriver.Chrome(options=WebGetDemo.Runmian(self).options())
        self.imgs = []
        # WebGetDemo.Runmian(self.driver).open('http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard')
        # WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        # pass
        self.driver.implicitly_wait(5)

    def add_img(self):
        # 1、下面注释掉的这行代码作用是不管用例是否执行成功，只要在执行过程加了self.add_img()操作，那么最后生成的报告中含有该执行过程的截图，如果不添加则默认对用例失败进行截图
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def tearDown(self):
        self.driver.refresh()

    def test_01(self):
        '''创新主体-随机切换企业类型'''
        try:
            time.sleep(3)
            # 点击创新发展下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header/div[1]/ul/div[1]/div[5]/li/div[1]/i')
            time.sleep(3)
            # 选择创新主体
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(3)
            # 点击企业类型下拉选择框
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="app"]/div/div/section/div/div[2]/span/button/span')
            time.sleep(3)
            # 随机切换一个企业类型
            num = random.randint(1, 9)
            js = 'document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择企业类型的class值
            js2 = 'return document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('is-checked', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_02(self):
        '''创新主体-随机切换大中小企业'''
        try:
            # time.sleep(3)
            # # 点击创新发展下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(6) > li > div > i')
            # time.sleep(3)
            # # 选择创新主体
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(1) > a > li')
            time.sleep(3)
            # 点击企业类型下拉选择框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div/div/span/span/i')
            time.sleep(3)
            # 随机切换一个企业类型
            num = random.randint(1, 4)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择企业类型的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_03(self):
        '''创新成果-随机切换专利'''
        try:
            time.sleep(3)
            # 点击创新发展下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header/div[1]/ul/div[1]/div[5]/li/div[1]/i')
            time.sleep(3)
            # 选择创新成果
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(3)
            # 点击专利下拉选择框
            WebGetDemo.Runmian(self.driver).click('xpath','//*[@id="app"]/div/div/section/div/div[2]/span/button/span')
            time.sleep(3)
            # 随机切换一个专利
            num = random.randint(1, 6)
            js = 'document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择企业类型的class值
            js2 = 'return document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('is-checked', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_04(self):
        '''创新成果-随机切换大中小企业'''
        try:
            # time.sleep(3)
            # # 点击创新发展下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(6) > li > div > i')
            # time.sleep(3)
            # # 选择创新成果
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li')
            time.sleep(3)
            # 点击大中小企业下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[1]/div/span/span/i')
            time.sleep(3)
            # 随机切换一个条件
            num = random.randint(5, 8)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择企业类型的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_05(self):
        '''创新成果-随机切换产业'''
        try:
            # time.sleep(3)
            # # 点击创新发展下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(6) > li > div > i')
            # time.sleep(3)
            # # 选择创新成果
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li')
            time.sleep(3)
            # 点击产业下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div[1]/span/span/i')
            time.sleep(3)
            # 随机切换一个条件
            num = random.randint(6, 8)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择企业类型的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
