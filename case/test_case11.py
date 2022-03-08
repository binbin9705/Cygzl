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
class Test11(unittest.TestCase):
    '''社会效益'''

    @classmethod
    def setUpClass(cls):
        # 启动浏览并设置相关选项
        cls.driver = webdriver.Chrome(options=WebGetDemo.Runmian(cls).options())
        # cls.imgs = []
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
        #刷新页面
        self.driver.refresh()
        self.driver.implicitly_wait(5)


    def add_img(self):
        # 1、下面注释掉的这行代码作用是不管用例是否执行成功，只要在执行过程加了self.add_img()操作，那么最后生成的报告中含有该执行过程的截图，如果不添加则默认对用例失败进行截图
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def tearDown(self):
        # WebGetDemo.Runmian(self.driver).quit()
        pass
    # @unittest.skip('跳过')
    def test_01(self):
        '''社会效益-总体概览-随机选择行业'''
        try:
            time.sleep(3)
            # 点击社会效益
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[4]/li/div/i')
            time.sleep(3)
            # 点击总体概览
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(3)
            # 点击行业下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/div[1]/button/span/i')
            time.sleep(3)
            # 随机选择一个行业
            num = random.randint(0, 19)
            js = 'document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择行业的class
            js2 = 'return document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('is-checked', classvalue, '用例执行失败')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[3]/div/button/span')
            time.sleep(2)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_02(self):
        '''社会效益-总体概览-随机选择产业'''
        try:
            # time.sleep(3)
            # # 点击社会效益
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[4]/li/div/i')
            # time.sleep(3)
            # # 点击总体概览
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(3)
            # 点击产业下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/div[2]/button/span/i')
            time.sleep(3)
            # 随机选择一个产业
            num = random.randint(0, 11)
            js = 'document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择行业的class
            js2 = 'return document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('is-checked', classvalue, '用例执行失败')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[3]/div/button/span')
            time.sleep(2)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_03(self):
        '''社会效益-结构分析-随机选择地区'''
        try:
            time.sleep(3)
            # 点击社会效益
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[4]/li/div/i')
            time.sleep(3)
            # 点击结构分析
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(3)
            # 随机选择一个地区
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/button/span/i')
            time.sleep(2)
            # 清空
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tipMul"]/div/div[2]/button[1]/span')
            time.sleep(2)
            num = random.randint(0, 11)
            js = 'document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            js3 = 'return document.getElementsByClassName("el-checkbox__label")[' + str(num) + '].innerText'
            textvalue = self.driver.execute_script(js3)
            js4 = 'return document.getElementsByClassName("selectM")[3].innerText'
            yxtext = self.driver.execute_script(js4)
            yxtext = yxtext.rstrip()
            self.assertEqual(yxtext, textvalue, '用例执行失败')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tipMul"]/div/div[2]/button[2]/span')
            time.sleep(2)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_04(self):
        '''社会效益-结构分析-随机选择行业'''
        try:
            # time.sleep(3)
            # # 点击社会效益
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[4]/li/div/i')
            # time.sleep(3)
            # # 点击结构分析
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/div[2]/button/span/i')
            time.sleep(2)
            num = random.randint(0, 19)
            js = 'document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            js2 = 'return document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[3]/div/button/span')
            time.sleep(2)
            self.assertIn('is-checked', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_05(self):
        '''社会效益-结构分析-随机选择产业'''
        try:
            # time.sleep(3)
            # # 点击社会效益
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[4]/li/div/i')
            # time.sleep(3)
            # # 点击结构分析
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/div[3]/button/span/i')
            time.sleep(2)
            num = random.randint(0, 11)
            js = 'document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            js2 = 'return document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/div[1]/div[3]/div/div/div[3]/div/button/span')
            time.sleep(2)
            self.assertIn('is-checked', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_06(self):
        '''社会效益-结构分析-统计图切换行业占比'''
        try:
            # time.sleep(3)
            # # 点击社会效益
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[4]/li/div/i')
            # time.sleep(3)
            # # 点击结构分析
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="jgfn_box_m"]/div[2]/div[1]/div/span/span/i')
            time.sleep(2)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[1].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[1].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('selected',classvalue,'用例执行失败')
        except Exception:
            self.add_img()
            raise


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
