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
class Test5(unittest.TestCase):
    '''产业结构模块页面交互'''

    @classmethod
    def setUpClass(cls):
        # 消除警告
        warnings.simplefilter('ignore', ResourceWarning)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # 启动浏览并设置相关选项
        self.driver = webdriver.Chrome(options=WebGetDemo.Runmian(self).options())
        self.imgs = []
        WebGetDemo.Runmian(self.driver).open('http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard')
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        self.driver.implicitly_wait(5)

    def add_img(self):
        # 1、下面注释掉的这行代码作用是不管用例是否执行成功，只要在执行过程加了self.add_img()操作，那么最后生成的报告中含有该执行过程的截图，如果不添加则默认对用例失败进行截图
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def tearDown(self):
        WebGetDemo.Runmian(self.driver).quit()

    def test_01(self):
        '''产业结构-总体监测-页面交互'''
        try:
            time.sleep(3)
            # 点击产业结构下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(4) > li > div > i')
            time.sleep(3)
            # 点击整体概览
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div:nth-child(6) > ul > div:nth-child(1) > a > li > span')
            # 断言是否正确跳转页面
            self.assertEqual('总体监测 - 产业高质量发展平台', self.driver.title, '未跳转指定页面')
            time.sleep(2)
            # 跳转数据表单页面
            js = 'document.getElementsByClassName("el-tabs__item is-top")[1].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取数据表单的class值
            js2 = 'return document.getElementsByClassName("el-tabs__item is-top")[1].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            # 判断数据表单是否为切换后状态
            self.assertIn('is-active', classvalue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_02(self):
        '''产业结构-结构监测-页面交互'''
        try:
            time.sleep(3)
            # 点击产业结构下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(4) > li > div > i')
            time.sleep(3)
            # 点击整体概览
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div:nth-child(6) > ul > div:nth-child(1) > a > li > span')
            time.sleep(3)
            # 点击机构监测
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > div > section > div > div.menu-List > a:nth-child(2)')
            time.sleep(2)
            # 跳转数据表单页面
            js = 'document.getElementsByClassName("el-tabs__item is-top")[1].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取数据表单的class值
            js2 = 'return document.getElementsByClassName("el-tabs__item is-top")[1].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            # 判断数据表单是否为切换后状态
            self.assertIn('is-active', classvalue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_03(self):
        '''产业结构-结构分析-随机年份展示统计图'''
        try:
            time.sleep(3)
            # 点击产业结构下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(4) > li > div > i')
            time.sleep(3)
            # 点击整体概览
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div:nth-child(6) > ul > div:nth-child(1) > a > li > span')
            time.sleep(3)
            # 点击结构监测
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > div > section > div > div.menu-List > a:nth-child(3)')
            time.sleep(2)
            # 点击年份下拉框
            js = 'document.getElementsByClassName("el-select__caret")[2].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 随机切换年份
            num = random.randint(0, 4)
            js2 = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js2)
            time.sleep(2)
            # 获取点击年份的class值
            js3 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js3)
            # 判断点击年份是否为切换后状态
            self.assertIn('selected', classvalue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_04(self):
        '''产业结构-结构分析-随机地区展示统计图'''
        try:
            time.sleep(3)
            # 点击产业结构下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(4) > li > div > i')
            time.sleep(3)
            # 点击整体概览
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div:nth-child(6) > ul > div:nth-child(1) > a > li > span')
            time.sleep(3)
            # 点击结构分析
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > div > section > div > div.menu-List > a:nth-child(3)')
            time.sleep(2)
            # 点击地区选择弹窗
            js = 'document.getElementsByClassName("el-select__caret")[3].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 点击清空
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#tipMul > div > div.flexRight.el-row > button.el-button.el-button--info.el-button--mini > span')
            time.sleep(2)
            # 随机选择一个地区
            num = random.randint(0, 33)
            js2 = 'document.getElementsByClassName("el-checkbox__inner")[' + str(num) + '].click()'
            self.driver.execute_script(js2)
            time.sleep(2)
            # 获取选择地区的class值
            js3 = 'return document.getElementsByClassName("el-checkbox__input")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js3)
            # 判断地区是否被选中
            self.assertIn('is-checked', classvalue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_05(self):
        '''产业结构-产业分析-本地数据统计图随机切换行业类型'''
        try:
            time.sleep(3)
            # 点击产业结构下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(4) > li > div > i')
            time.sleep(3)
            # 点击产业分析
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div:nth-child(6) > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 随机切换一个产业
            num = random.randint(1, 11)
            js = 'document.querySelector("#pane-BDSJ > div > div.monitor-left > ul > li:nth-child(' + str(
                num) + ')").click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择产业的class值
            js2 = 'return document.querySelector("#pane-BDSJ > div > div.monitor-left > ul > li:nth-child(' + str(
                num) + ')").getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            # 判断地区是否被选中
            self.assertIn('active', classvalue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_06(self):
        '''产业结构-产业分析-切换区域对比统计图'''
        try:
            time.sleep(3)
            # 点击产业结构下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(4) > li > div > i')
            time.sleep(3)
            # 点击产业分析
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div:nth-child(6) > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 切换区域对比
            WebGetDemo.Runmian(self.driver).click('id', 'tab-JGFX')
            time.sleep(2)
            # 获取区域对比的class
            classvalue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'id', 'tab-JGFX')
            # 判断地区是否被选中
            self.assertIn('active', classvalue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_07(self):
        '''产业结构-产业分析-区域对比随机选择地区'''
        try:
            time.sleep(3)
            # 点击产业结构下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(4) > li > div > i')
            time.sleep(3)
            # 点击产业分析
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div:nth-child(6) > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 切换区域对比
            WebGetDemo.Runmian(self.driver).click('id', 'tab-JGFX')
            time.sleep(3)
            # 点击地区选择弹窗
            WebGetDemo.Runmian(self.driver).click('css', '#pane-JGFX > div > div.control-main > div > i')
            time.sleep(3)
            # 点击清空
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#tipMul > div > div.flexRight.el-row > button.el-button.el-button--info.el-button--mini > span')
            time.sleep(2)
            # 随机选择一个地区
            num = random.randint(0, 33)
            js = 'document.getElementsByClassName("el-checkbox__inner")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取点击地区的class值
            js2 = 'return document.getElementsByClassName("el-checkbox__input")[' + str(
                num) + '].getAttribute("class")'
            calssvalue = self.driver.execute_script(js2)
            # 判断地区是否被选中
            self.assertIn('is-checked', calssvalue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_08(self):
        '''产业结构-产业分析-区域对比随机选择行业'''
        try:
            time.sleep(3)
            # 点击产业结构下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(4) > li > div > i')
            time.sleep(3)
            # 点击产业分析
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div:nth-child(6) > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 切换区域对比
            WebGetDemo.Runmian(self.driver).click('id', 'tab-JGFX')
            time.sleep(2)
            # 随机选择一个行业
            num = random.randint(2, 11)
            js = 'document.querySelector("#pane-JGFX > div > div.monitor-main > div.monitor-left > ul > li:nth-child(' + str(
                num) + ')").click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择行业的class值
            js2 = 'return document.querySelector("#pane-JGFX > div > div.monitor-main > div.monitor-left > ul > li:nth-child(' + str(
                num) + ')").getAttribute("class")'
            calssvalue = self.driver.execute_script(js2)
            # 判断地区是否被选中
            self.assertIn('active', calssvalue, '用例执行错误')
        except Exception:
            self.add_img()
            raise


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
