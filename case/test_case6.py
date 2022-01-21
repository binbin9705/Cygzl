import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo
import warnings
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


# @unittest.skip('调试')
class Test6(unittest.TestCase):
    '''市场主体模块页面交互'''

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

    def add_img(self):
        # 1、下面注释掉的这行代码作用是不管用例是否执行成功，只要在执行过程加了self.add_img()操作，那么最后生成的报告中含有该执行过程的截图，如果不添加则默认对用例失败进行截图
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def tearDown(self):
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过'
    def test_01(self):
        '''企业总量企业列表页面交互-按照币种'阿富汗尼'查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击币种标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(10) > span > button > span')
            time.sleep(3)
            # 点击阿富汗尼
            js = 'document.getElementsByClassName("el-checkbox__inner")[103].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="pane-企业列表"]/div/div[5]/div[2]/div/div[2]/button[2]/span')
            baidu_input = (By.XPATH, '//*[@id="pane-企业列表"]/div/div[6]/div/div[3]/table/tbody/tr[2]/td[2]')
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(baidu_input))
            time.sleep(3)
            # 获取已选条件中的值
            classvlue = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                                   '//*[@id="pane-企业列表"]/div/div[1]/div[2]/div/span/span')
            time.sleep(3)
            # 判断已选条件框中的值是否等于前者选择的条件
            self.assertEqual(classvlue, '阿富汗尼', '用例执行错误')
        except Exception:
            self.add_img()
            # 该语句引发当前上下文中捕获的异常
            raise

    #@unittest.skip('跳过'
    def test_02(self):
        '''企业总量企业列表页面交互-按照币种'欧元'查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击币种标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(10) > span > button > span')
            time.sleep(3)
            # 点击欧元
            js = 'document.getElementsByClassName("el-checkbox__inner")[104].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="pane-企业列表"]/div/div[5]/div[2]/div/div[2]/button[2]/span')
            time.sleep(3)
            # 获取已选条件中的值
            classvlue = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                                   '//*[@id="pane-企业列表"]/div/div[1]/div[2]/div/span/span')
            time.sleep(3)
            # 判断已选条件框中的值是否等于前者选择的条件
            self.assertEqual(classvlue, '欧元', '用例执行错误')
        except Exception:
            self.add_img()
            # 该语句引发当前上下文中捕获的异常
            raise

    #@unittest.skip('跳过'
    def test_03(self):
        '''企业总量企业列表页面交互-按照币种'日元'查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击币种标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(10) > span > button > span')
            time.sleep(3)
            # 点击日元
            js = 'document.getElementsByClassName("el-checkbox__inner")[105].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="pane-企业列表"]/div/div[5]/div[2]/div/div[2]/button[2]/span')
            time.sleep(3)
            # 获取已选条件中的值
            classvlue = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                                   '//*[@id="pane-企业列表"]/div/div[1]/div[2]/div/span/span')
            time.sleep(3)
            # 判断已选条件框中的值是否等于前者选择的条件
            self.assertEqual(classvlue, '日元', '用例执行错误')
        except Exception:
            self.add_img()
            # 该语句引发当前上下文中捕获的异常
            raise

    #@unittest.skip('跳过'
    def test_04(self):
        '''企业总量企业列表页面交互-按照币种'澳大利亚元'查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击币种标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(10) > span > button > span')
            time.sleep(3)
            # 点击澳大利亚元
            js = 'document.getElementsByClassName("el-checkbox__inner")[106].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="pane-企业列表"]/div/div[5]/div[2]/div/div[2]/button[2]/span')
            time.sleep(3)
            # 获取已选条件中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                                   '//*[@id="pane-企业列表"]/div/div[1]/div[2]/div/span/span')
            time.sleep(3)
            self.assertEqual(testvalue, '澳大利亚元', '用例执行不通过')
        except Exception:
            self.add_img()
            # 该语句引发当前上下文中捕获的异常
            raise

    #@unittest.skip('跳过'
    def test_05(self):
        '''企业总量企业列表页面交互-按照币种‘英镑’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击币种标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(10) > span > button > span')
            time.sleep(3)
            # 点击英镑
            js = 'document.getElementsByClassName("el-checkbox__inner")[107].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '英镑', '用例执行不通过')
        except Exception:
            self.add_img()
            # 该语句引发当前上下文中捕获的异常
            raise

    #@unittest.skip('跳过'
    def test_06(self):
        '''企业总量企业列表页面交互-按照币种‘新加坡元’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击币种标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(10) > span > button > span')
            time.sleep(3)
            # 点击新加坡元
            js = 'document.getElementsByClassName("el-checkbox__inner")[108].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '新加坡元', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_07(self):
        '''企业总量企业列表页面交互-按照币种‘加元’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击币种标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(10) > span > button > span')
            time.sleep(3)
            # 点击加元
            js = 'document.getElementsByClassName("el-checkbox__inner")[109].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '加元', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_08(self):
        '''企业总量企业列表页面交互-按照币种‘瑞士法郎’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击币种标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(10) > span > button > span')
            time.sleep(3)
            # 点击瑞士法郎
            js = 'document.getElementsByClassName("el-checkbox__inner")[110].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '瑞士法郎', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_09(self):
        '''企业总量企业列表页面交互-按照综合实力‘AAA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击综合实力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(1) > span > button > span')
            time.sleep(3)
            # 点击AAA
            js = 'document.getElementsByClassName("el-checkbox__inner")[101].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '综合实力 AAA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_10(self):
        '''企业总量企业列表页面交互-按照综合实力‘AA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击综合实力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(1) > span > button > span')
            time.sleep(3)
            # 点击AA
            js = 'document.getElementsByClassName("el-checkbox__inner")[102].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '综合实力 AA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_11(self):
        '''企业总量企业列表页面交互-按照综合实力‘A’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击综合实力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(1) > span > button > span')
            time.sleep(3)
            # 点击A
            js = 'document.getElementsByClassName("el-checkbox__inner")[103].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '综合实力 A', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_12(self):
        '''企业总量企业列表页面交互-按照综合实力‘BBB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击综合实力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(1) > span > button > span')
            time.sleep(3)
            # 点击BBB
            js = 'document.getElementsByClassName("el-checkbox__inner")[104].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '综合实力 BBB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_13(self):
        '''企业总量企业列表页面交互-按照综合实力‘BB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击综合实力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(1) > span > button > span')
            time.sleep(3)
            # 点击BB
            js = 'document.getElementsByClassName("el-checkbox__inner")[105].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '综合实力 BB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_14(self):
        '''企业总量企业列表页面交互-按照综合实力‘B’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击综合实力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(1) > span > button > span')
            time.sleep(3)
            # 点击B
            js = 'document.getElementsByClassName("el-checkbox__inner")[106].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '综合实力 B', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_15(self):
        '''企业总量企业列表页面交互-按照综合实力‘CCC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击综合实力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(1) > span > button > span')
            time.sleep(3)
            # 点击CCC
            js = 'document.getElementsByClassName("el-checkbox__inner")[107].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '综合实力 CCC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_16(self):
        '''企业总量企业列表页面交互-按照综合实力‘CC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击综合实力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(1) > span > button > span')
            time.sleep(3)
            # 点击CC
            js = 'document.getElementsByClassName("el-checkbox__inner")[108].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '综合实力 CC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_17(self):
        '''企业总量企业列表页面交互-按照综合实力‘C’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击综合实力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(1) > span > button > span')
            time.sleep(3)
            # 点击C
            js = 'document.getElementsByClassName("el-checkbox__inner")[109].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '综合实力 C', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_18(self):
        '''企业总量企业列表页面交互-按照综合实力‘D’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击综合实力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(1) > span > button > span')
            time.sleep(3)
            # 点击D
            js = 'document.getElementsByClassName("el-checkbox__inner")[110].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '综合实力 D', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_19(self):
        '''企业总量企业列表页面交互-按照合法合规‘AAA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(2) > span > button > span')
            time.sleep(3)
            # 点击AAA
            js = 'document.getElementsByClassName("el-checkbox__inner")[101].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '合法合规 AAA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_20(self):
        '''企业总量企业列表页面交互-按照合法合规‘AA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(2) > span > button > span')
            time.sleep(3)
            # 点击AA
            js = 'document.getElementsByClassName("el-checkbox__inner")[102].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '合法合规 AA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_21(self):
        '''企业总量企业列表页面交互-按照合法合规‘A’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(2) > span > button > span')
            time.sleep(3)
            # 点击A
            js = 'document.getElementsByClassName("el-checkbox__inner")[103].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '合法合规 A', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_22(self):
        '''企业总量企业列表页面交互-按照合法合规‘BBB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(2) > span > button > span')
            time.sleep(3)
            # 点击BBB
            js = 'document.getElementsByClassName("el-checkbox__inner")[104].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '合法合规 BBB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_23(self):
        '''企业总量企业列表页面交互-按照合法合规‘BB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(2) > span > button > span')
            time.sleep(3)
            # 点击BB
            js = 'document.getElementsByClassName("el-checkbox__inner")[105].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '合法合规 BB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_24(self):
        '''企业总量企业列表页面交互-按照合法合规‘B’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(2) > span > button > span')
            time.sleep(3)
            # 点击B
            js = 'document.getElementsByClassName("el-checkbox__inner")[106].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '合法合规 B', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_25(self):
        '''企业总量企业列表页面交互-按照合法合规‘CCC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(2) > span > button > span')
            time.sleep(3)
            # 点击CCC
            js = 'document.getElementsByClassName("el-checkbox__inner")[107].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '合法合规 CCC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_26(self):
        '''企业总量企业列表页面交互-按照合法合规‘CC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(2) > span > button > span')
            time.sleep(3)
            # 点击CC
            js = 'document.getElementsByClassName("el-checkbox__inner")[108].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '合法合规 CC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_27(self):
        '''企业总量企业列表页面交互-按照合法合规‘C’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(2) > span > button > span')
            time.sleep(3)
            # 点击C
            js = 'document.getElementsByClassName("el-checkbox__inner")[109].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '合法合规 C', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_28(self):
        '''企业总量企业列表页面交互-按照合法合规‘D’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(2) > span > button > span')
            time.sleep(3)
            # 点击D
            js = 'document.getElementsByClassName("el-checkbox__inner")[110].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '合法合规 D', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_29(self):
        '''企业总量企业列表页面交互-按照创新能力‘AAA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(3) > span > button > span')
            time.sleep(3)
            # 点击AAA
            js = 'document.getElementsByClassName("el-checkbox__inner")[101].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '创新能力 AAA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_30(self):
        '''企业总量企业列表页面交互-按照创新能力‘AA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(3) > span > button > span')
            time.sleep(3)
            # 点击AA
            js = 'document.getElementsByClassName("el-checkbox__inner")[102].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '创新能力 AA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_31(self):
        '''企业总量企业列表页面交互-按照创新能力‘A’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(3) > span > button > span')
            time.sleep(3)
            # 点击A
            js = 'document.getElementsByClassName("el-checkbox__inner")[103].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '创新能力 A', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_32(self):
        '''企业总量企业列表页面交互-按照创新能力‘BBB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(3) > span > button > span')
            time.sleep(3)
            # 点击BBB
            js = 'document.getElementsByClassName("el-checkbox__inner")[104].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '创新能力 BBB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_33(self):
        '''企业总量企业列表页面交互-按照创新能力‘BB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(3) > span > button > span')
            time.sleep(3)
            # 点击BB
            js = 'document.getElementsByClassName("el-checkbox__inner")[105].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '创新能力 BB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_34(self):
        '''企业总量企业列表页面交互-按照创新能力‘B’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(3) > span > button > span')
            time.sleep(3)
            # 点击B
            js = 'document.getElementsByClassName("el-checkbox__inner")[106].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '创新能力 B', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_35(self):
        '''企业总量企业列表页面交互-按照创新能力‘CCC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(3) > span > button > span')
            time.sleep(3)
            # 点击CCC
            js = 'document.getElementsByClassName("el-checkbox__inner")[107].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '创新能力 CCC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_36(self):
        '''企业总量企业列表页面交互-按照创新能力‘CC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(3) > span > button > span')
            time.sleep(3)
            # 点击CC
            js = 'document.getElementsByClassName("el-checkbox__inner")[108].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '创新能力 CC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_37(self):
        '''企业总量企业列表页面交互-按照创新能力‘C’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(3) > span > button > span')
            time.sleep(3)
            # 点击C
            js = 'document.getElementsByClassName("el-checkbox__inner")[109].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '创新能力 C', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_38(self):
        '''企业总量企业列表页面交互-按照创新能力‘D’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击合法合规筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(3) > span > button > span')
            time.sleep(3)
            # 点击D
            js = 'document.getElementsByClassName("el-checkbox__inner")[110].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '创新能力 D', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_39(self):
        '''企业总量企业列表页面交互-按照社会贡献‘AAA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击社会贡献筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(4) > span > button > span')
            time.sleep(3)
            # 点击AAA
            js = 'document.getElementsByClassName("el-checkbox__inner")[101].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '社会贡献 AAA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_40(self):
        '''企业总量企业列表页面交互-按照社会贡献‘AA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击社会贡献筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(4) > span > button > span')
            time.sleep(3)
            # 点击AA
            js = 'document.getElementsByClassName("el-checkbox__inner")[102].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '社会贡献 AA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_41(self):
        '''企业总量企业列表页面交互-按照社会贡献‘A’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击社会贡献筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(4) > span > button > span')
            time.sleep(3)
            # 点击A
            js = 'document.getElementsByClassName("el-checkbox__inner")[103].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '社会贡献 A', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_42(self):
        '''企业总量企业列表页面交互-按照社会贡献‘BBB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击社会贡献筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(4) > span > button > span')
            time.sleep(3)
            # 点击BBB
            js = 'document.getElementsByClassName("el-checkbox__inner")[104].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '社会贡献 BBB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_43(self):
        '''企业总量企业列表页面交互-按照社会贡献‘BB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击社会贡献筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(4) > span > button > span')
            time.sleep(3)
            # 点击BB
            js = 'document.getElementsByClassName("el-checkbox__inner")[105].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '社会贡献 BB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_44(self):
        '''企业总量企业列表页面交互-按照社会贡献‘B’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击社会贡献筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(4) > span > button > span')
            time.sleep(3)
            # 点击B
            js = 'document.getElementsByClassName("el-checkbox__inner")[106].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '社会贡献 B', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_45(self):
        '''企业总量企业列表页面交互-按照社会贡献‘CCC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击社会贡献筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(4) > span > button > span')
            time.sleep(3)
            # 点击CCC
            js = 'document.getElementsByClassName("el-checkbox__inner")[107].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '社会贡献 CCC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_46(self):
        '''企业总量企业列表页面交互-按照社会贡献‘CC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击社会贡献筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(4) > span > button > span')
            time.sleep(3)
            # 点击CC
            js = 'document.getElementsByClassName("el-checkbox__inner")[108].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '社会贡献 CC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_47(self):
        '''企业总量企业列表页面交互-按照社会贡献‘C’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击社会贡献筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(4) > span > button > span')
            time.sleep(3)
            # 点击C
            js = 'document.getElementsByClassName("el-checkbox__inner")[109].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '社会贡献 C', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_48(self):
        '''企业总量企业列表页面交互-按照社会贡献‘D’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击社会贡献筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(4) > span > button > span')
            time.sleep(3)
            # 点击D
            js = 'document.getElementsByClassName("el-checkbox__inner")[110].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '社会贡献 D', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_49(self):
        '''企业总量企业列表页面交互-按照发展潜力‘AAA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击发展潜力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(5) > span > button > span')
            time.sleep(3)
            # 点击AAA
            js = 'document.getElementsByClassName("el-checkbox__inner")[101].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '发展潜力 AAA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_50(self):
        '''企业总量企业列表页面交互-按照发展潜力‘AA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击发展潜力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(5) > span > button > span')
            time.sleep(3)
            # 点击AA
            js = 'document.getElementsByClassName("el-checkbox__inner")[102].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '发展潜力 AA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_51(self):
        '''企业总量企业列表页面交互-按照发展潜力‘A’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击发展潜力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(5) > span > button > span')
            time.sleep(3)
            # 点击A
            js = 'document.getElementsByClassName("el-checkbox__inner")[103].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '发展潜力 A', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_52(self):
        '''企业总量企业列表页面交互-按照发展潜力‘BBB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击发展潜力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(5) > span > button > span')
            time.sleep(3)
            # 点击BBB
            js = 'document.getElementsByClassName("el-checkbox__inner")[104].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '发展潜力 BBB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_53(self):
        '''企业总量企业列表页面交互-按照发展潜力‘BB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击发展潜力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(5) > span > button > span')
            time.sleep(3)
            # 点击BB
            js = 'document.getElementsByClassName("el-checkbox__inner")[105].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '发展潜力 BB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_54(self):
        '''企业总量企业列表页面交互-按照发展潜力‘B’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击发展潜力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(5) > span > button > span')
            time.sleep(3)
            # 点击B
            js = 'document.getElementsByClassName("el-checkbox__inner")[106].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '发展潜力 B', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_55(self):
        '''企业总量企业列表页面交互-按照发展潜力‘CCC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击发展潜力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(5) > span > button > span')
            time.sleep(3)
            # 点击CCC
            js = 'document.getElementsByClassName("el-checkbox__inner")[107].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '发展潜力 CCC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_56(self):
        '''企业总量企业列表页面交互-按照发展潜力‘CC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击发展潜力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(5) > span > button > span')
            time.sleep(3)
            # 点击CC
            js = 'document.getElementsByClassName("el-checkbox__inner")[108].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '发展潜力 CC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_57(self):
        '''企业总量企业列表页面交互-按照发展潜力‘C’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击发展潜力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(5) > span > button > span')
            time.sleep(3)
            # 点击C
            js = 'document.getElementsByClassName("el-checkbox__inner")[109].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '发展潜力 C', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_58(self):
        '''企业总量企业列表页面交互-按照发展潜力‘D’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击发展潜力筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(5) > span > button > span')
            time.sleep(3)
            # 点击D
            js = 'document.getElementsByClassName("el-checkbox__inner")[110].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '发展潜力 D', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_59(self):
        '''企业总量企业列表页面交互-按照企业效率‘AAA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击企业效率筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(6) > span > button > span')
            time.sleep(3)
            # 点击AAA
            js = 'document.getElementsByClassName("el-checkbox__inner")[101].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '企业效率 AAA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_60(self):
        '''企业总量企业列表页面交互-按照企业效率‘AA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击企业效率筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(6) > span > button > span')
            time.sleep(3)
            # 点击AA
            js = 'document.getElementsByClassName("el-checkbox__inner")[102].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '企业效率 AA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_61(self):
        '''企业总量企业列表页面交互-按照企业效率‘A’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击企业效率筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(6) > span > button > span')
            time.sleep(3)
            # 点击A
            js = 'document.getElementsByClassName("el-checkbox__inner")[103].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '企业效率 A', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_62(self):
        '''企业总量企业列表页面交互-按照企业效率‘BBB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击企业效率筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(6) > span > button > span')
            time.sleep(3)
            # 点击BBB
            js = 'document.getElementsByClassName("el-checkbox__inner")[104].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '企业效率 BBB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_63(self):
        '''企业总量企业列表页面交互-按照企业效率‘BB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击企业效率筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(6) > span > button > span')
            time.sleep(3)
            # 点击BB
            js = 'document.getElementsByClassName("el-checkbox__inner")[105].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '企业效率 BB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_64(self):
        '''企业总量企业列表页面交互-按照企业效率‘B’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击企业效率筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(6) > span > button > span')
            time.sleep(3)
            # 点击B
            js = 'document.getElementsByClassName("el-checkbox__inner")[106].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '企业效率 B', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_65(self):
        '''企业总量企业列表页面交互-按照企业效率‘CCC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击企业效率筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(6) > span > button > span')
            time.sleep(3)
            # 点击CCC
            js = 'document.getElementsByClassName("el-checkbox__inner")[107].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '企业效率 CCC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_66(self):
        '''企业总量企业列表页面交互-按照企业效率‘CC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击企业效率筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(6) > span > button > span')
            time.sleep(3)
            # 点击CC
            js = 'document.getElementsByClassName("el-checkbox__inner")[108].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '企业效率 CC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_67(self):
        '''企业总量企业列表页面交互-按照企业效率‘C’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击企业效率筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(6) > span > button > span')
            time.sleep(3)
            # 点击C
            js = 'document.getElementsByClassName("el-checkbox__inner")[109].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '企业效率 C', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_68(self):
        '''企业总量企业列表页面交互-按照企业效率‘D’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击企业效率筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(6) > span > button > span')
            time.sleep(3)
            # 点击D
            js = 'document.getElementsByClassName("el-checkbox__inner")[110].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '企业效率 D', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_69(self):
        '''企业总量企业列表页面交互-按照活跃度‘AAA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击活跃度筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(7) > span > button > span')
            time.sleep(3)
            # 点击AAA
            js = 'document.getElementsByClassName("el-checkbox__inner")[101].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '活跃度 AAA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_70(self):
        '''企业总量企业列表页面交互-按照活跃度‘AA’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击活跃度筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(7) > span > button > span')
            time.sleep(3)
            # 点击AA
            js = 'document.getElementsByClassName("el-checkbox__inner")[102].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '活跃度 AA', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_71(self):
        '''企业总量企业列表页面交互-按照活跃度‘A’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击活跃度筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(7) > span > button > span')
            time.sleep(3)
            # 点击A
            js = 'document.getElementsByClassName("el-checkbox__inner")[103].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '活跃度 A', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_72(self):
        '''企业总量企业列表页面交互-按照活跃度‘BBB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击活跃度筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(7) > span > button > span')
            time.sleep(3)
            # 点击BBB
            js = 'document.getElementsByClassName("el-checkbox__inner")[104].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '活跃度 BBB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_73(self):
        '''企业总量企业列表页面交互-按照活跃度‘BB’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击活跃度筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(7) > span > button > span')
            time.sleep(3)
            # 点击BB
            js = 'document.getElementsByClassName("el-checkbox__inner")[105].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '活跃度 BB', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_74(self):
        '''企业总量企业列表页面交互-按照活跃度‘B’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击活跃度筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(7) > span > button > span')
            time.sleep(3)
            # 点击B
            js = 'document.getElementsByClassName("el-checkbox__inner")[106].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '活跃度 B', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_75(self):
        '''企业总量企业列表页面交互-按照活跃度‘CCC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击活跃度筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(7) > span > button > span')
            time.sleep(3)
            # 点击CCC
            js = 'document.getElementsByClassName("el-checkbox__inner")[107].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '活跃度 CCC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_76(self):
        '''企业总量企业列表页面交互-按照活跃度‘CC’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击活跃度筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(7) > span > button > span')
            time.sleep(3)
            # 点击CC
            js = 'document.getElementsByClassName("el-checkbox__inner")[108].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '活跃度 CC', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_77(self):
        '''企业总量企业列表页面交互-按照活跃度‘C’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击活跃度筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(7) > span > button > span')
            time.sleep(3)
            # 点击C
            js = 'document.getElementsByClassName("el-checkbox__inner")[109].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '活跃度 C', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_78(self):
        '''企业总量企业列表页面交互-按照活跃度‘D’查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击活跃度筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(7) > span > button > span')
            time.sleep(3)
            # 点击D
            js = 'document.getElementsByClassName("el-checkbox__inner")[110].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获取已选条件框中的值
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div > span > span')
            time.sleep(3)
            self.assertEqual(testvalue, '活跃度 D', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_79(self):
        '''企业总量企业列表页面交互-随机排序方式降序查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击排序方式筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(4) > div.el-col.el-col-22 > div > div:nth-child(1) > div > span > span')
            time.sleep(3)
            # 随机点击排序字段
            num = random.randint(5, 13)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            # 获得点击字段的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertEqual(classvalue, 'el-select-dropdown__item selected hover', '用例执行不通过')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_80(self):
        '''企业总量企业列表页面交互-随机排序方式升序查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击排序方式筛选标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(4) > div.el-col.el-col-22 > div > div:nth-child(1) > div > span > span')
            time.sleep(3)
            # 随机点击排序字段
            num = random.randint(5, 13)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 获得点击字段的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            time.sleep(3)
            # 点击升序
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="pane-企业列表"]/div/div[4]/div[2]/div/div[2]/div/span/span/i')
            js3 = 'document.getElementsByClassName("el-select-dropdown__item")[13].click()'
            self.driver.execute_script(js3)
            time.sleep(3)
            # 获取升序的的class值
            js4 = 'return document.getElementsByClassName("el-select-dropdown__item")[13].getAttribute("class")'
            classvalue2 = self.driver.execute_script(js4)
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            self.assertEqual(classvalue, 'el-select-dropdown__item selected hover', '用例执行不通过')
            self.assertEqual(classvalue2, 'el-select-dropdown__item selected hover', '用例执行不通过，未选择升序')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_81(self):
        '''企业总量企业列表页面交互-关键字’北京‘查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 获取列表条数
            listnumber = WebGetDemo.Runmian(self.driver).obtaintest('class_name', 'el-pagination__total')
            time.sleep(3)
            # 点击文本框输入关键词
            WebGetDemo.Runmian(self.driver).input_data('xpath',
                                                       '//*[@id="pane-企业列表"]/div/div[5]/div[2]/div/div[1]/input','北京')
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            newlistnumber = WebGetDemo.Runmian(self.driver).obtaintest('class_name', 'el-pagination__total')
            self.assertNotEqual(newlistnumber,listnumber,'用例执行失败查询关键词后列表数据无变化')
        except Exception:
            self.add_img()
            raise

    #@unittest.skip('跳过'
    def test_82(self):
        '''企业总量企业列表页面交互-关键字’郑州‘查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 获取列表条数
            listnumber = WebGetDemo.Runmian(self.driver).obtaintest('class_name', 'el-pagination__total')
            time.sleep(3)
            # 点击文本框输入关键词
            WebGetDemo.Runmian(self.driver).input_data('xpath',
                                                       '//*[@id="pane-企业列表"]/div/div[5]/div[2]/div/div[1]/input',
                                                       '郑州')
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            newlistnumber = WebGetDemo.Runmian(self.driver).obtaintest('class_name', 'el-pagination__total')
            self.assertNotEqual(newlistnumber, listnumber, '用例执行失败查询关键词后列表数据无变化')
        except Exception:
            self.add_img()
            raise



if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
