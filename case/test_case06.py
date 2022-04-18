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
class Test06(unittest.TestCase):
    '''产业地图'''

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
        '''产业地图-页面交互-随机选择产业'''
        try:
            time.sleep(3)
            # 点击产业地图
            WebGetDemo.Runmian(self.driver).click('xpath','//*[@id="app"]/div/header/div[1]/ul/div[1]/div[4]/a/li/span')
            time.sleep(3)
            # 点击产业下拉选择框
            js = 'document.querySelector("#app > div > div > section > div > div.in-map-control > div > button").click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 随机选择一个产业
            num = random.randint(1, 8)
            js2 = 'document.getElementsByClassName("el-checkbox__inner")[' + str(num) + '].click()'
            self.driver.execute_script(js2)
            # 获取点击产业的text值
            js3 = 'return document.getElementsByClassName("el-tree-node__label")[' + str(num) + '].innerText'
            textvalue = self.driver.execute_script(js3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > div > section > div > div.in-map-control > div > div > div > div.el-dialog__footer > div > button')
            time.sleep(3)
            # 获取统计图上方显示行业text
            js4 = 'return document.querySelector("#app > div > div > section > div > div.in-map-control > div > button > span").innerText'
            # rstrip去除字符串右侧空格
            textvalue2 = self.driver.execute_script(js4)
            textvalue2 = textvalue2.rstrip()
            self.assertEqual(textvalue2, textvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_02(self):
        '''产业地图-页面交互-切换统计图中地区'''
        try:
            # time.sleep(3)
            # # 点击产业地图
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(5) > a > li > span')
            time.sleep(3)
            # 点击统计图中的中国
            js1 = 'document.getElementsByClassName("el-radio__input")[1].click()'
            self.driver.execute_script(js1)
            time.sleep(2)
            # 获取点击条件的class值
            js2 = 'return document.getElementsByClassName("el-radio__input")[1].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('is-checked', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_03(self):
        '''产业地图-页面交互-随机切换统计信息条件'''
        try:
            # time.sleep(3)
            # # 点击产业地图
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(5) > a > li > span')
            time.sleep(3)
            # 随机点击一个统计信息中的条件
            num = random.randint(3, 4)
            js1 = 'document.getElementsByClassName("el-radio-button__inner")[' + str(num) + '].click()'
            self.driver.execute_script(js1)
            time.sleep(2)
            # 获取点击条件的class值
            js2 = 'return document.getElementsByClassName("el-radio-button el-radio-button--mini")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('is-active', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_04(self):
        '''产业地图-页面交互-随机切换发展态势统计图年份'''
        try:
            # time.sleep(3)
            # # 点击产业地图
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(5) > a > li > span')
            time.sleep(3)
            # 随机点击一个年份
            num = random.randint(5, 14)
            js1 = 'document.getElementsByClassName("el-radio-button el-radio-button--mini")[' + str(num) + '].click()'
            self.driver.execute_script(js1)
            time.sleep(2)
            # 获取点击条件的class值
            js2 = 'return document.getElementsByClassName("el-radio-button el-radio-button--mini")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('is-active', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_05(self):
        '''产业地图-页面交互-产业发展统计图切换统计条件'''
        try:
            # time.sleep(3)
            # # 点击产业地图
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(5) > a > li > span')
            time.sleep(3)
            # 切换注册资本
            js1 = 'document.getElementsByClassName("el-radio-button el-radio-button--mini")[17].click()'
            self.driver.execute_script(js1)
            time.sleep(2)
            # 获取点击条件的class值
            js2 = 'return document.getElementsByClassName("el-radio-button el-radio-button--mini")[17].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('is-active', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
