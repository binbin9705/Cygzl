import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo
import warnings


class Test4(unittest.TestCase):
    '''首页页面交互1'''

    @classmethod
    def setUpClass(cls):
        # 消除警告
        warnings.simplefilter('ignore', ResourceWarning)
        # pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # 启动浏览并设置相关选项
        self.driver = webdriver.Chrome(options=WebGetDemo.Runmian(self).options())
        self.driver.maximize_window()
        WebGetDemo.Runmian(self.driver).open('http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard')
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')

    def tearDown(self):
        WebGetDemo.Runmian(self.driver).quit()

    # @unittest.skip('跳过')
    def test_01(self):
        '''市场主体统计图切换统计条件-高薪企业'''
        self.driver.implicitly_wait(5)
        try:
            # 先获取高薪企业class值
            classvalue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath',
                                                                     '//*[@id="app"]/div/div/section/div/div[2]/div[1]/div[1]/label[2]')
            # 点击市场主体中的高新企业
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  ' //*[@id="app"]/div/div/section/div/div[2]/div[1]/div[1]/label[2]/span ')
            time.sleep(3)
            afterclassvalue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath',
                                                                          '//*[@id="app"]/div/div/section/div/div[2]/div[1]/div[1]/label[2]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertNotEqual(classvalue, afterclassvalue, '用例执行错误')

    # @unittest.skip('跳过')
    def test_02(self):
        '''市场主体统计图切换统计条件-战兴企业'''
        self.driver.implicitly_wait(5)
        try:
            # 先获取战兴企业class值
            classvalue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath',
                                                                     '//*[@id="app"]/div/div/section/div/div[2]/div[1]/div[1]/label[3]')
            # 点击统计图中的战兴企业 战兴企业
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div[1]/div[1]/label[3]/span')
            time.sleep(3)
            afterclassvalue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath',
                                                                          '//*[@id="app"]/div/div/section/div/div[2]/div[1]/div[1]/label[3]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertNotEqual(classvalue, afterclassvalue, '用例执行错误点击后元素值应该发生变化')

    # @unittest.skip('跳过')
    def test_03(self):
        '''切换地区-天津市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[2]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('天津市', ys, '用例执行错误')




if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
