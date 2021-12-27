import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo

import warnings


class Test4(unittest.TestCase):
    '''首页页面交互-统计图切换统计条件'''

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

    @unittest.skip('跳过')
    def test_03(self):
        '''左上角搜索'''
        self.driver.implicitly_wait(5)
        # try:
        WebGetDemo.Runmian(self.driver).click('xpath','//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[1]/input')
        time.sleep(2)
        WebGetDemo.Runmian(self.driver).input_data('xpath','//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[1]/input','淘数')
        time.sleep(3)
        WebGetDemo.Runmian(self.driver).click('xpath','//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[2]/div[1]/div[1]/ul/li[1]/span')
        time.sleep(3)
        #获得所有句丙
        allhandel=self.driver.window_handles
        #切换句丙
        self.driver.switch_to.window(allhandel[1])
        time.sleep(2)
        #切换frame
        self.driver.switch_to.frame('com_frame')
        #新页面操作
        WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="mapMainBox"]/body/div[3]/div[2]/div/div/div/ul[2]/li/div/div[1]/div[1]/ul/li[2]')
        time.sleep(2)

        # except AssertionError as e:
        #     # 调用封装好的截图方法，进行截图并保存在本地磁盘
        #     WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        # except Exception as e:
        #     WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        # self.assertEqual('天津市', ys, '用例执行错误')




if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
