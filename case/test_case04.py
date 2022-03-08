import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo
import warnings
import random


# @unittest.skip('调试')
class Test04(unittest.TestCase):
    '''市场主体'''

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
        pass

    def setUp(self):
        # # 启动浏览并设置相关选项
        # self.driver = webdriver.Chrome(options=WebGetDemo.Runmian(self).options())
        self.imgs = []
        # WebGetDemo.Runmian(self.driver).open('http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard')
        # WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        # pass
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
        '''CRI指数页面统计图切换统计条件-年度数据'''
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            time.sleep(3)
            # 点击CRI指数
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(1) > a > li > span')
            time.sleep(3)
            # 点击统计条件下来选择框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > div > section > div > div.localDiv > div.formeList > div > div > span > span > i')
            time.sleep(3)
            # 点击年度数据
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')
            time.sleep(3)
            # 获取年度数据的class值
            classvalue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath',
                                                                     '/html/body/div[3]/div[1]/div[1]/ul/li[1]')
            # 判断有没有正常跳转页面
            self.assertEqual(self.driver.title, 'CRI指数 - 产业高质量发展平台', '用例执行错误')
            # 判断点击年度数据 弹窗class值有没有发生变化
            self.assertEqual(classvalue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_02(self):
        '''企业总量页面本地数据统计图交互-按照存量企业数量'''
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # 点击企业总量
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击统计条件下拉框
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="pane-本地数据"]/div/div/div/div[1]/div[1]/div[1]')
            time.sleep(3)
            # 取消新增企业数量选中存量企业数量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(2) > span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(1) > span')
            time.sleep(3)
            # 获取存量企业数量的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(1)')
            # 判断有没有正常跳转页面
            self.assertEqual(self.driver.title, '企业总量 - 产业高质量发展平台', '用例执行错误')
            # 判断存量企业数量的class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_03(self):
        '''企业总量页面本地数据统计图交互-按照新增企业注册资本'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            #
            # # 点击企业总量
            # time.sleep(3)
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击统计条件下拉框
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="pane-本地数据"]/div/div/div/div[1]/div[1]/div[1]')
            time.sleep(3)
            # 取消选中新增企业数量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(2) > span')
            time.sleep(3)
            # 选中注册资本指标-新增企业注册资本
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(2) > li:nth-child(2) > ul > li:nth-child(2) > span')
            time.sleep(3)
            # 获取新增企业注册资本的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(2) > li:nth-child(2) > ul > li:nth-child(2)')
            # 判断有没有正常跳转页面
            self.assertEqual(self.driver.title, '企业总量 - 产业高质量发展平台', '用例执行错误')
            # 判断新增企业注册资本的class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_04(self):
        '''企业总量页面本地数据统计图交互-按照年度数据'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            #
            # # 点击企业总量
            # time.sleep(3)
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击年度月度统计条件下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-本地数据 > div > div > div > div.formeList > div:nth-child(2) > div.el-input.el-input--suffix > span > span > i')
            # 选中年度数据
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span')
            # 获取年度数据的class值
            time.sleep(3)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)')
            # 判断有没有正常跳转页面
            self.assertEqual(self.driver.title, '企业总量 - 产业高质量发展平台', '用例执行错误')
            # 判断class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_05(self):
        '''企业总量页面统计图切换统计模块-区域对比'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击区域对比
            WebGetDemo.Runmian(self.driver).click('id', 'tab-区域对比')
            time.sleep(3)
            # 获取区域对比div的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'id', 'tab-区域对比')
            # 获取区域对比div的tabindex值
            tabindexvlue = WebGetDemo.Runmian(self.driver).obtainvalue('tabindex', 'id', 'tab-区域对比')
            # 判断有没有正常跳转页面
            self.assertEqual(self.driver.title, '企业总量 - 产业高质量发展平台', '用例执行错误')
            # 判断点击区域对比后对应div的class值有没有发生变化
            self.assertEqual(classvlue, 'el-tabs__item is-top is-active', '用例执行错误')
            # 判断点击区域对比后对应div的tabindex值有没有发生变化
            self.assertNotEqual(tabindexvlue, '-1', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_06(self):
        '''企业总量页面本区域对比统计图交互-按照新增企业数量展示统计图'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击区域对比
            WebGetDemo.Runmian(self.driver).click('id', 'tab-区域对比')
            time.sleep(3)
            # 点击企业数量指标下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-区域对比 > div > div > div > div.formeList > div:nth-child(1) > div.el-input.el-input--suffix > span > span > i')
            time.sleep(3)
            # 点击新增企业数量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(2)')
            time.sleep(3)
            # 获取新增企业数量的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(2)')
            time.sleep(3)
            # 判断class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_07(self):
        '''企业总量页面本区域对比统计图交互-按照新增企业注册资本展示统计图'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击区域对比
            WebGetDemo.Runmian(self.driver).click('id', 'tab-区域对比')
            time.sleep(3)
            # 点击企业数量指标下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-区域对比 > div > div > div > div.formeList > div:nth-child(1) > div.el-input.el-input--suffix > span > span > i')
            time.sleep(3)
            # 点击新增企业注册资本
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(2) > li:nth-child(2) > ul > li:nth-child(2)')
            time.sleep(3)
            # 获取点击的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(2) > li:nth-child(2) > ul > li:nth-child(2)')
            time.sleep(3)
            # 判断class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_08(self):
        '''企业总量页面本区域对比统计图交互-按照年度数据展示统计图'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击区域对比
            WebGetDemo.Runmian(self.driver).click('id', 'tab-区域对比')
            time.sleep(3)
            # 点击时间维度下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-区域对比 > div > div > div > div.formeList > div:nth-child(2) > div > span > span > i')
            time.sleep(3)
            # 点击年度数据
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)')
            time.sleep(3)
            # 获取点击的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)')
            time.sleep(3)
            # 判断class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_09(self):
        '''企业总量页面统计图切换统计模块-企业列表'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击区域对比
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 获取区域对比div的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'id', 'tab-企业列表')
            # 获取区域对比div的tabindex值
            tabindexvlue = WebGetDemo.Runmian(self.driver).obtainvalue('tabindex', 'id', 'tab-企业列表')
            # 判断有没有正常跳转页面
            self.assertEqual(self.driver.title, '企业总量 - 产业高质量发展平台', '用例执行错误')
            # 判断点击区域对比后对应div的class值有没有发生变化
            self.assertEqual(classvlue, 'el-tabs__item is-top is-active', '用例执行错误')
            # 判断点击区域对比后对应div的tabindex值有没有发生变化
            self.assertNotEqual(tabindexvlue, '-1', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_10(self):
        '''企业总量企业列表页面交互-随机经营状态查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击经营状态下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(1) > span')
            time.sleep(3)
            # 点击随机一个经营状态
            num = random.randint(107, 110)
            js = 'document.getElementsByClassName("el-checkbox__inner")[' + str(num) + '].click()'
            # 获取点击经营状态的文本值
            js2 = 'return document.getElementsByClassName("el-tree-node__label")[' + str(num) + '].innerText'
            classvalue = self.driver.execute_script(js2)
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
            self.assertEqual(classvlue, classvalue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_11(self):
        '''企业总量企业列表页面交互-按照成立时间'1978年以前'查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击成立时间下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > div:nth-child(2) > button > span')
            time.sleep(3)
            # 点击1978年以前
            js = 'document.getElementsByClassName("el-checkbox__inner")[4].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击弹出框的确定
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="pane-企业列表"]/div/div[2]/div[2]/div/div[1]/div/div/div[3]/div/button')
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
            self.assertEqual(classvlue, '1978年以前', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_12(self):
        '''企业总量企业列表页面交互-按照国标行业'农、林、牧、渔业'查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击国标行业标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > div:nth-child(4) > button > span')
            time.sleep(3)
            # 点击农、林、牧、渔业
            js = 'document.getElementsByClassName("el-checkbox__inner")[4].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击弹出框的确定
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="pane-企业列表"]/div/div[2]/div[2]/div/div[3]/div/div/div[3]/div/button')
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
            self.assertEqual(classvlue, '农、林、牧、渔业', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_13(self):
        '''企业总量企业列表页面交互-按照注册资本'10亿以上'查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击注册资本标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(5) > span > button > span')
            time.sleep(3)
            # 点击10亿以上
            js = 'document.getElementsByClassName("el-checkbox__inner")[103].click()'
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
            self.assertEqual(classvlue, '10亿以上', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_14(self):
        '''企业总量企业列表页面交互-按照企业类型'国有企业'查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击企业类型标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(6) > span > button > span')
            time.sleep(3)
            # 点击国有企业
            js = 'document.getElementsByClassName("el-checkbox__inner")[103].click()'
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
            self.assertEqual(classvlue, '国有企业', '用例执行错误')
        except Exception:
            self.add_img()
            # 该语句引发当前上下文中捕获的异常
            raise

    def test_15(self):
        '''企业总量企业列表页面交互-按照优质企业'国有企业'查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击优质企业标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(7) > span > button > span')
            time.sleep(3)
            # 点击国有企业
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
            self.assertEqual(classvlue, '国有企业', '用例执行错误')
        except Exception:
            self.add_img()
            # 该语句引发当前上下文中捕获的异常
            raise

    def test_16(self):
        '''企业总量企业列表页面交互-按照企业规模'大型企业'查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击企业规模标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(8) > span > button > span')
            # 点击大型企业
            js = 'document.getElementsByClassName("el-checkbox__inner")[107].click()'
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
            self.assertEqual(classvlue, '大型企业', '用例执行错误')
        except Exception:
            self.add_img()
            # 该语句引发当前上下文中捕获的异常
            raise

    def test_17(self):
        '''企业总量企业列表页面交互-按照产业领域'三大产业'查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击产业领域标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > div:nth-child(9) > button > span')
            time.sleep(3)
            # 点击三大产业
            js = 'document.getElementsByClassName("el-checkbox__inner")[31].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击弹出框中的确定
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="pane-企业列表"]/div/div[2]/div[2]/div/div[4]/div/div/div[3]/div/button/span')
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
            self.assertEqual(classvlue, '三大产业', '用例执行错误')
        except Exception:
            self.add_img()
            # 该语句引发当前上下文中捕获的异常
            raise

    def test_18(self):
        '''企业总量企业列表页面交互-按照币种'美元'查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击币种标签
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(10) > span > button > span')
            time.sleep(3)
            # 点击美元
            js = 'document.getElementsByClassName("el-checkbox__inner")[101].click()'
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
            self.assertEqual(classvlue, '美元', '用例执行错误')
        except Exception:
            self.add_img()
            # 该语句引发当前上下文中捕获的异常
            raise

    def test_19(self):
        '''企业总量企业列表页面交互-按照综合实力‘AAA’查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
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

    def test_20(self):
        '''企业总量企业列表页面交互-按照合法合规‘B’查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
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

    def test_21(self):
        '''企业总量企业列表页面交互-按照创新能力‘A’查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
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

    def test_22(self):
        '''企业总量企业列表页面交互-按照社会贡献‘CCC’查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
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

    def test_23(self):
        '''企业总量企业列表页面交互-按照发展潜力‘AAA’查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
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

    def test_24(self):
        '''企业总量企业列表页面交互-按照企业效率‘AAA’查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
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

    def test_25(self):
        '''企业总量企业列表页面交互-按照活跃度‘AAA’查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
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

    def test_26(self):
        '''企业总量企业列表页面交互-随机排序方式降序查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
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

    def test_27(self):
        '''企业总量企业列表页面交互-随机排序方式升序查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
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

    def test_28(self):
        '''企业总量企业列表页面交互-关键字’北京‘查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 获取列表条数
            listnumber = WebGetDemo.Runmian(self.driver).obtaintest('class_name', 'el-pagination__total')
            time.sleep(3)
            # 点击文本框输入关键词
            WebGetDemo.Runmian(self.driver).input_data('xpath',
                                                       '//*[@id="pane-企业列表"]/div/div[5]/div[2]/div/div[1]/input', '北京')
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

    def test_29(self):
        '''企业总量企业列表页面交互-关键字’郑州‘查询企业'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
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

    def test_30(self):
        '''企业总量企业列表页面交互-关键字’~！@#￥%……&*‘查询企业'''
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击文本框输入关键词
            WebGetDemo.Runmian(self.driver).input_data('xpath',
                                                       '//*[@id="pane-企业列表"]/div/div[5]/div[2]/div/div[1]/input',
                                                       '~！@#￥%……&*')
            time.sleep(3)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button.el-button.bgColorLR.el-button--primary > span')
            time.sleep(3)
            calsstest = WebGetDemo.Runmian(self.driver).obtaintest('class_name', 'el-table__empty-text')
            self.assertEqual(calsstest, '暂无数据', '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_31(self):
        '''企业总量企业列表页面交互-翻页随机跳转企业详情'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(2)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 随机翻页2-6页
            number = random.randint(2, 6)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div.formeList.tableRow.el-row > div > ul > li:nth-child(' + str(
                                                      number) + ')')
            time.sleep(3)
            # 跳转随机一个企业并获取企业名称
            num = random.randint(1, 20)
            qytest = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                "#pane-企业列表 > div > div:nth-child(6) > div > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(" + str(
                                                                    num) + ") > td.el-table_1_column_2.listEntName.el-table__cell > div")
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  "#pane-企业列表 > div > div:nth-child(6) > div > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(" + str(
                                                      num) + ") > td.el-table_1_column_2.listEntName.el-table__cell > div")
            time.sleep(3)
            # 切换到新title页
            WebGetDemo.Runmian(self.driver).switch_window_by_title('企业大数据')
            # 切换到新的frame里
            WebGetDemo.Runmian(self.driver).switch_window_by_frame('com_frame')
            time.sleep(3)
            newqytest = WebGetDemo.Runmian(self.driver).obtaintest('class_name', 'p_entName')
            time.sleep(3)
            self.assertEqual(newqytest, qytest, '用例执行错误')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).switch_window_by_title('企业总量 - 产业高质量发展平台')
        except Exception:
            self.add_img()
            raise

    def test_32(self):
        '''企业总量企业列表页面交互-清空筛选条件-随机经营状态标签'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 选中随机一个经营状态
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(1) > span > button > span')
            time.sleep(3)
            num = random.randint(107, 110)
            js = 'document.getElementsByClassName("el-checkbox__inner")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击清空
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button:nth-child(1) > span')
            time.sleep(3)
            yxtest = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div')
            self.assertEqual(yxtest, '暂无', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_33(self):
        '''企业总量企业列表页面交互-清空筛选条件-随机任意指标'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            num = random.randint(1, 7)
            # 选中随机一个指标
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(3) > div.el-col.el-col-22 > div > span:nth-child(' + str(
                                                      num) + ') > span > button > span')
            time.sleep(3)
            zbnum = random.randint(101, 110)
            js = 'document.getElementsByClassName("el-checkbox__inner")[' + str(zbnum) + '].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击清空
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(5) > div.el-col.el-col-22 > div > div.iconBox > button:nth-child(1) > span')
            time.sleep(3)
            yxtest = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                '#pane-企业列表 > div > div:nth-child(1) > div.el-col.el-col-22 > div')
            self.assertEqual(yxtest, '暂无', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_34(self):
        '''企业总量企业列表页面交互-列表按照100条/页展示'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击企业总量
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击企业列表
            WebGetDemo.Runmian(self.driver).click('id', 'tab-企业列表')
            time.sleep(3)
            # 点击分页标签
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="pane-企业列表"]/div/div[7]/div/span[2]/div/div/span/span/i')
            time.sleep(3)
            # 选择100条/页
            js = 'document.getElementsByClassName("el-select-dropdown__item")[13].click()'
            self.driver.execute_script(js)
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[3]/span')
            time.sleep(3)
            yxtest = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                                '//*[@id="pane-企业列表"]/div/div[6]/div/div[3]/table/tbody/tr[100]/td[1]/div/div')
            self.assertEqual(yxtest, '100', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_35(self):
        '''行业分析整体概况页面交互-随机统计类型展示统计图'''
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击主体分析
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(3) > a > li > span')
            time.sleep(3)
            # 点击企业数量指标下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-整体概况 > div > div.formeList > div:nth-child(1) > div > input')
            time.sleep(3)
            # 随机选择一个指标
            num = random.randint(2, 4)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            # 获取点击后指标的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            time.sleep(3)
            self.assertEqual(classvalue, 'el-select-dropdown__item selected', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_36(self):
        '''行业分析整体概况页面交互-按行业门类着色展示统计图'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击主体分析
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(3) > a > li > span')
            # time.sleep(3)
            # 点击统计图风格下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-整体概况 > div > div.formeList > div:nth-child(2) > div > span > span > i')
            time.sleep(3)
            # 选择行业门类着色
            js = 'document.getElementsByClassName("el-select-dropdown__item")[4].click()'
            self.driver.execute_script(js)
            # 获取行业门类的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[4].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            time.sleep(3)
            self.assertEqual(classvalue, 'el-select-dropdown__item selected', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_37(self):
        '''行业分析整体概况页面交互-随机行业展示统计图/清空'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击主体分析
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(3) > a > li > span')
            # time.sleep(3)
            # 点击行业选择弹窗
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-整体概况 > div > div.formeList > button > span')
            time.sleep(3)
            # 随机选择一个行业
            num = random.randint(0, 19)
            js = 'document.getElementsByClassName("el-checkbox__inner")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 获取选择行业的文本值
            js2 = 'return document.getElementsByClassName("el-tree-node__label")[' + str(num) + '].innerText'
            classvalue = self.driver.execute_script(js2)
            # 获取已选中的文本值
            js3 = 'return document.getElementsByClassName("selectM")[4].innerText'
            xclassvalue = self.driver.execute_script(js3)
            # 已选栏中+有空格 rstrip去除字符串右侧空格
            Selectedvalue = xclassvalue.rstrip()
            self.assertEqual(classvalue, Selectedvalue, '用例执行错误')
            time.sleep(2)
            # 点击清空
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="pane-整体概况"]/div/div[1]/div[3]/div/div[2]/div/section/footer/button[1]/span')
            # 获取已选的文本
            xztext = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                                '//*[@id="pane-整体概况"]/div/div[1]/div[3]/div/div[2]/div/section/main/h4/p')
            self.assertEqual(xztext, '已选:(0/20)', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_38(self):
        '''行业分析行业分类页面交互-随机统计类型展示统计图'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击主体分析
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(3) > a > li > span')
            time.sleep(3)
            # 切换行业分类模块
            WebGetDemo.Runmian(self.driver).click('id', 'tab-行业分类')
            time.sleep(3)
            # 点击企业数量指标下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#dataList > div:nth-child(1) > div > span > span > i')
            time.sleep(3)
            # 随机选择一个指标
            num = random.randint(7, 9)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 获取点击后指标的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            time.sleep(3)
            self.assertEqual(classvalue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_39(self):
        '''行业分析行业分类页面交互-按行业门类着色展示统计图'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击主体分析
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(3) > a > li > span')
            time.sleep(3)
            # 切换行业分类模块
            WebGetDemo.Runmian(self.driver).click('id', 'tab-行业分类')
            time.sleep(3)
            # 点击统计图风格下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#dataList > div:nth-child(2) > div.el-input.el-input--suffix > span > span > i')
            time.sleep(3)
            # 选择行业门类着色
            js = 'document.getElementsByClassName("el-select-dropdown__item")[9].click()'
            self.driver.execute_script(js)
            # 获取行业门类的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[9].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            time.sleep(3)
            self.assertEqual(classvalue, 'el-select-dropdown__item selected', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_40(self):
        '''行业分析行业分类页面交互-随机年份展示统计图'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击主体分析
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(3) > a > li > span')
            time.sleep(3)
            # 切换行业分类模块
            WebGetDemo.Runmian(self.driver).click('id', 'tab-行业分类')
            time.sleep(3)
            # 点击年份下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#dataList > div:nth-child(3) > div > span > span > i')
            time.sleep(3)
            # 随机选择一个年份
            num = random.randint(5, 9)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            # 获取选择年份的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            time.sleep(3)
            self.assertEqual(classvalue, 'el-select-dropdown__item selected', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_41(self):
        '''行业分析整体概况页面交互-随机行业展示统计图/清空'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击主体分析
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(3) > a > li > span')
            # time.sleep(3)
            # 切换行业分类模块
            WebGetDemo.Runmian(self.driver).click('id', 'tab-行业分类')
            time.sleep(3)
            # 点击行业选择弹窗
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#dataList > button > span')
            time.sleep(3)
            # 随机选择一个行业
            num = random.randint(0, 19)
            js = 'document.getElementsByClassName("el-checkbox__inner")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 获取选择行业的文本值
            js2 = 'return document.getElementsByClassName("el-tree-node__label")[' + str(num) + '].innerText'
            classvalue = self.driver.execute_script(js2)
            # 获取已选中的文本值
            js3 = 'return document.getElementsByClassName("selectM")[5].innerText'
            xclassvalue = self.driver.execute_script(js3)
            # 已选栏中+有空格 rstrip去除字符串右侧空格
            Selectedvalue = xclassvalue.rstrip()
            self.assertEqual(classvalue, Selectedvalue, '用例执行错误')
            time.sleep(2)
            # 点击清空
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="dataList"]/div[4]/div/div[2]/div/section/footer/button[1]/span')
            time.sleep(2)
            # 获取已选的文本
            xztext = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                                '//*[@id="dataList"]/div[4]/div/div[2]/div/section/main/h4/p')
            self.assertEqual(xztext, '已选:(0/20)', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_42(self):
        '''结构分析页面交互-随机企业数量指标展示统计图'''
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击结构分析
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(4) > a > li > span')
            time.sleep(3)
            # 点击企业数量指标下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > div > section > div > div.localDiv > div.formeList > div:nth-child(1) > div > span > span > i')
            time.sleep(3)
            # 随机选择一个指标
            num = random.randint(4, 9)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            # 获取选择指标的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            time.sleep(2)
            self.assertEqual(classvalue, 'el-select-dropdown__item selected', '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_43(self):
        '''结构分析页面交互-按月度数据展示统计图'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击结构分析
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(4) > a > li > span')
            # time.sleep(3)
            # 点击年月选择下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > div > section > div > div.localDiv > div.formeList > div:nth-child(2) > div > span > span > i')
            time.sleep(3)
            # 选择月度数据
            js = 'document.getElementsByClassName("el-select-dropdown__item")[9].click()'
            self.driver.execute_script(js)
            # 获取月度数据的class
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[9].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertEqual(classvalue, 'el-select-dropdown__item selected', '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_44(self):
        '''结构分析页面交互-随机地区展示统计图'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击结构分析
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(4) > a > li > span')
            # time.sleep(3)
            # 点击地区选择弹出框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > div > section > div > div.localDiv > div.formeList > button > span')
            time.sleep(3)
            # 点击清空
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#tipMul > div > div.flexRight.el-row > button.el-button.el-button--info.el-button--mini > span')
            time.sleep(2)
            yxtext = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                '#tipMul > div > div.trimListBox > p:nth-child(1) > span:nth-child(2)')
            self.assertEqual(yxtext, '(0/40)', '点击清空后数据未清除')
            # 快捷点击东部地区
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#tipMul > div > div.trimListBox > p:nth-child(3) > button > span')
            time.sleep(2)
            yxtext2 = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                 '#tipMul > div > div.trimListBox > p:nth-child(1) > span:nth-child(2)')
            self.assertEqual(yxtext2, '(10/40)', '选择快捷标签未选择地区')
        except Exception:
            self.add_img()
            raise

    def test_45(self):
        '''结构分析页面交互-随机行业展示统计图'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击结构分析
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(4) > a > li > span')
            # time.sleep(3)
            # 点击行业选择弹出框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > div > section > div > div.localDiv > div.formeList > div:nth-child(5) > button > span')
            time.sleep(3)
            # 随机选择一个行业
            num = random.randint(0, 19)
            js = 'document.getElementsByClassName("el-checkbox__input")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择行业的文本
            js2 = 'return document.getElementsByClassName("el-tree-node__label")[' + str(num) + '].innerText'
            text = self.driver.execute_script(js2)
            time.sleep(2)
            # 点击确定
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > div > section > div > div.localDiv > div.formeList > div:nth-child(5) > div > div > div.el-dialog__footer > div > button > span')
            time.sleep(2)
            # 获取行业选择框的文本值
            text2 = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                               '#app > div > div > section > div > div.localDiv > div.formeList > div:nth-child(5) > button > span')
            self.assertEqual(text, text2, '用例执行错误选择行业错误')
        except Exception:
            self.add_img()
            raise

    def test_46(self):
        '''结构分析页面交互-统计图切换行业占比'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击结构分析
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(4) > a > li > span')
            # time.sleep(3)
            # 点击区域占比下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#jgfn_box_m > div:nth-child(2) > div.el-select.selectM > div > span > span > i')
            time.sleep(3)
            # 选择行业占比
            js = 'document.getElementsByClassName("el-select-dropdown__item")[9].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取行业占比的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[9].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_47(self):
        '''重点企业页面交互-随机统计类型展示统计图'''
        try:
            # 点击市场主体下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            time.sleep(3)
            # 点击重点企业
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(5) > a > li > span')
            time.sleep(3)
            # 点击统计图筛选条件下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-占比监测 > div > div.formeList > div > div.el-input.el-input--suffix > input')
            time.sleep(3)
            # 随机选择战略新兴或上市企业
            num = random.randint(1, 2)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择条件得的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_48(self):
        '''重点企业区域对比页面交互-随机统计类型展示统计图'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击重点企业
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(5) > a > li > span')
            # time.sleep(3)
            # 点击区域对比
            WebGetDemo.Runmian(self.driver).click('id', 'tab-1')
            time.sleep(3)
            # 点击统计图筛选条件下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-1 > div > div.formeList > div.el-select.selectM > div.el-input.el-input--suffix > span > span > i')
            time.sleep(3)
            # 随机选择战略新兴或上市企业
            num = random.randint(1, 2)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择条件得的class值
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_49(self):
        '''重点企业区域对比页面交互-随机选择地区'''
        try:
            # # 点击市场主体下拉框
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')
            # time.sleep(3)
            # # 点击重点企业
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       'body > div.el-menu--horizontal > ul > div:nth-child(5) > a > li > span')
            # time.sleep(3)
            # 点击区域对比
            WebGetDemo.Runmian(self.driver).click('id', 'tab-1')
            time.sleep(3)
            # 点击地区选择弹出框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-1 > div > div.formeList > button > span')
            time.sleep(3)
            # 点击清空
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#tipMul > div > div.flexRight.el-row > button.el-button.el-button--info.el-button--mini > span')
            # 获取已选条件的文本
            text = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                              '#tipMul > div > div.trimListBox > p:nth-child(1) > span:nth-child(2)')
            self.assertEqual(text, '(0/40)', '用例执行失败')
            time.sleep(2)
            # 随机选择一个地区
            num = random.randint(0, 33)
            js = 'document.getElementsByClassName("el-checkbox__inner")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            # 获取选择条件得的文本值
            js2 = 'return document.getElementsByClassName("el-checkbox__label")[' + str(
                num) + '].innerText'
            text2 = self.driver.execute_script(js2)
            # 获取已选条件框中条件的文本
            js3 = 'return document.getElementsByClassName("selectM")[4].innerText'
            text3 = self.driver.execute_script(js3)
            # rstrip去除字符串右侧空格
            text3 = text3.rstrip()
            self.assertEqual(text3, text2, '用例执行失败')
        except Exception:
            self.add_img()
            raise


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
