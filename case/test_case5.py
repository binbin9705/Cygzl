import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo
import warnings


# @unittest.skip('调试')
class Test5(unittest.TestCase):
    '''市场主体页面交互'''

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

    # @unittest.skip('跳过')
    def test_01(self):
        '''CRI指数页面统计图切换统计条件-年度数据'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
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
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath',
                                                                    '/html/body/div[3]/div[1]/div[1]/ul/li[1]')
            # 判断有没有正常跳转页面
            self.assertEqual(self.driver.title, 'CRI指数 - 产业高质量发展平台', '用例执行错误')
            # 判断点击年度数据 弹窗class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_02(self):
        '''CRI指数页面统计图切换统计条件-月度数据'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
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
            # 点击月度数据
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')
            time.sleep(3)
            # 获取月度数据的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath',
                                                                    '/html/body/div[3]/div[1]/div[1]/ul/li[2]')
            # 判断有没有正常跳转页面
            self.assertEqual(self.driver.title, 'CRI指数 - 产业高质量发展平台', '用例执行错误')
            # 判断点击月度数据 弹窗class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_03(self):
        '''企业总量页面统计图切换统计模块-区域对比'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
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

    # @unittest.skip('跳过')
    def test_04(self):
        '''企业总量页面统计图切换统计模块-企业列表'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
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

    # @unittest.skip('跳过')
    def test_05(self):
        '''企业总量页面本地数据统计图交互-按照存量企业数量'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
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

    # @unittest.skip('跳过')
    def test_06(self):
        '''企业总量页面本地数据统计图交互-按照新增企业数量'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
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
            # 取消新增企业数量再次选中新增企业数量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(2) > span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(2) > span')
            time.sleep(3)
            # 获取新增企业数量的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(2)')
            # 判断有没有正常跳转页面
            self.assertEqual(self.driver.title, '企业总量 - 产业高质量发展平台', '用例执行错误')
            # 判断新增企业数量的class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_07(self):
        '''企业总量页面本地数据统计图交互-按照死亡企业数量'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
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
            # 取消新增企业数量选中死亡企业数量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(2) > span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(3) > span')
            time.sleep(3)
            # 获取死亡企业数量的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(3)')
            # 判断有没有正常跳转页面
            self.assertEqual(self.driver.title, '企业总量 - 产业高质量发展平台', '用例执行错误')
            # 判断死亡企业数量的class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_08(self):
        '''企业总量页面本地数据统计图交互-按照存量企业注册资本'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
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
            # 取消选中新增企业数量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(2) > span')
            time.sleep(3)
            # 选中注册资本指标-存量企业注册资本
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(2) > li:nth-child(2) > ul > li:nth-child(1) > span')
            time.sleep(3)
            # 获取存量企业注册资本的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(2) > li:nth-child(2) > ul > li:nth-child(1)')
            # 判断有没有正常跳转页面
            self.assertEqual(self.driver.title, '企业总量 - 产业高质量发展平台', '用例执行错误')
            # 判断存量企业注册资本的class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_09(self):
        '''企业总量页面本地数据统计图交互-按照新增企业注册资本'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
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

    # @unittest.skip('跳过')
    def test_10(self):
        '''企业总量页面本地数据统计图交互-按照死亡企业注册资本'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')

            # 点击企业总量
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击统计条件下拉框
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="pane-本地数据"]/div/div/div/div[1]/div[1]/div[1]')
            # 取消选中新增企业数量
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(2) > span')
            time.sleep(3)
            js = 'document.getElementsByClassName("el-scrollbar__wrap")[3].scrollTop=10000'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击死亡企业注册资本
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(2) > li:nth-child(2) > ul > li:nth-child(3) > span')
            time.sleep(3)
            # 获取死亡企业注册资本的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(2) > li:nth-child(2) > ul > li:nth-child(3)')
            # 判断有没有正常跳转页面
            self.assertEqual(self.driver.title, '企业总量 - 产业高质量发展平台', '用例执行错误')
            # 判断死亡企业注册资本的class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_11(self):
        '''企业总量页面本地数据统计图交互-按照年度数据'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')

            # 点击企业总量
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击年度月度统计条件下拉框
            time.sleep(3)
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

    # @unittest.skip('跳过')
    def test_12(self):
        '''企业总量页面本地数据统计图交互-按照月度数据'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i')

            # 点击企业总量
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            # 点击年度月度统计条件下拉框
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-本地数据 > div > div > div > div.formeList > div:nth-child(2) > div.el-input.el-input--suffix > span > span > i')
            # 选中年度数据
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span')
            # 点击年度月度统计条件下拉框
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-本地数据 > div > div > div > div.formeList > div:nth-child(2) > div.el-input.el-input--suffix > span > span > i')
            # 再选中月度数据
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2) > span')
            # 获取月度数据的class值
            time.sleep(3)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')
            # 判断有没有正常跳转页面
            self.assertEqual(self.driver.title, '企业总量 - 产业高质量发展平台', '用例执行错误')
            # 判断class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_13(self):
        '''企业总量页面本区域对比统计图交互-按照新增企业数量'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
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

    # @unittest.skip('跳过')
    def test_14(self):
        '''企业总量页面本区域对比统计图交互-按照死亡企业数量'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击区域对比
            WebGetDemo.Runmian(self.driver).click('id', 'tab-区域对比')
            time.sleep(3)
            # 点击企业数量指标下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-区域对比 > div > div > div > div.formeList > div:nth-child(1) > div.el-input.el-input--suffix > span > span > i')
            time.sleep(3)
            # 点击死亡企业数量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(3)')
            time.sleep(3)
            # 获取点击的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(1) > li:nth-child(2) > ul > li:nth-child(3)')
            time.sleep(3)
            # 判断class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_15(self):
        '''企业总量页面本区域对比统计图交互-按照存量企业注册资本'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击区域对比
            WebGetDemo.Runmian(self.driver).click('id', 'tab-区域对比')
            time.sleep(3)
            # 点击企业数量指标下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-区域对比 > div > div > div > div.formeList > div:nth-child(1) > div.el-input.el-input--suffix > span > span > i')
            time.sleep(3)
            # 点击存量企业注册资本
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(2) > li:nth-child(2) > ul > li:nth-child(1)')
            time.sleep(3)
            # 获取点击的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(2) > li:nth-child(2) > ul > li:nth-child(1)')
            time.sleep(3)
            # 判断class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_16(self):
        '''企业总量页面本区域对比统计图交互-按照新增企业注册资本'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
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

    # @unittest.skip('跳过')
    def test_17(self):
        '''企业总量页面本区域对比统计图交互-按照死亡企业注册资本'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
            # 点击区域对比
            WebGetDemo.Runmian(self.driver).click('id', 'tab-区域对比')
            time.sleep(3)
            # 点击企业数量指标下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-区域对比 > div > div > div > div.formeList > div:nth-child(1) > div.el-input.el-input--suffix > span > span > i')
            time.sleep(3)
            # 控制下拉框向下滑
            js = 'document.getElementsByClassName("el-scrollbar__wrap")[3].scrollTop=10000'
            self.driver.execute_script(js)
            time.sleep(3)
            # 点击死亡企业注册资本
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(2) > li:nth-child(2) > ul > li:nth-child(3)')
            time.sleep(3)
            # 获取点击的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ul:nth-child(2) > li:nth-child(2) > ul > li:nth-child(3)')
            time.sleep(3)
            # 判断class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_18(self):
        '''企业总量页面本区域对比统计图交互-按照年度数据'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
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

    # @unittest.skip('跳过')
    def test_19(self):
        '''企业总量页面本区域对比统计图交互-按照月度数据'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  ' #app > div > header.layout-header-fixed > div.header > ul > div.header-left > div:nth-child(3) > li > div > i ')
            time.sleep(3)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-menu--horizontal > ul > div:nth-child(2) > a > li > span')
            time.sleep(3)
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
            # 点击时间维度下拉框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-区域对比 > div > div > div > div.formeList > div:nth-child(2) > div > span > span > i')
            time.sleep(3)
            # 点击月度数据
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')
            time.sleep(3)
            # 获取点击的class值
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                    'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')
            time.sleep(3)
            # 判断class值有没有发生变化
            self.assertEqual(classvlue, 'el-select-dropdown__item selected hover', '用例执行错误')
        except Exception:
            self.add_img()
            raise

    # @unittest.skip('跳过')
    def test_20(self):
        '''企业总量企业列表页面交互-按照经营状态'新设'查询企业'''
        self.driver.implicitly_wait(5)
        try:
            # 点击市场主体下来框
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
            # 点击经营状态下来框
            WebGetDemo.Runmian(self.driver).click('css',
                                                  '#pane-企业列表 > div > div:nth-child(2) > div.el-col.el-col-22 > div > span:nth-child(1) > span')
            time.sleep(3)
            # 点击新设
            js = 'document.getElementsByClassName("el-checkbox__inner")[107].click();'
            self.driver.execute_script(js)
            time.sleep(3)
            # 获取已选条件中的值
            classvlue = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                                   '//*[@id="pane-企业列表"]/div/div[1]/div[2]/div/span/span')
            time.sleep(3)
            # 判断已选条件框中的值是否等于新设
            self.assertEqual(classvlue, '新设', '用例执行错误')
        except Exception:
            self.add_img()
            raise


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
