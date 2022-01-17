import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo
import warnings


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


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
