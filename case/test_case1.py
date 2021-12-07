import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo
import warnings
from selenium.webdriver.common.by import By

class Test1(unittest.TestCase):
    '''页面跳转'''
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # 启动浏览并设置相关选项
        self.driver = webdriver.Chrome(options=WebGetDemo.Runmian(self).options())
        self.driver.maximize_window()
        WebGetDemo.Runmian(self.driver).open('http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard')

    def tearDown(self):
        pass


    #@unittest.skip('跳过')
    def test_01(self):
        '''首页跳转CRL指数页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[2]/li/div/s1pan')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('CRI指数 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_02(self):
        '''首页跳转企业总量页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[2]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        # 判断跳转后的标签页是不是企业总量
        self.assertEqual('企业总量 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_03(self):
        '''首页跳转行业分析页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[2]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[3]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('行业分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_04(self):
        '''首页跳转结构分析页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[2]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[4]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('结构分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_05(self):
        '''首页跳转重点企业页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[2]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[5]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('重点企业 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_06(self):
        '''首页跳转总体监测页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[3]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('总体监测 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_07(self):
        '''首页跳转产业分析页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[3]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('产业分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_08(self):
        '''首页跳转产业地图页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[4]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('产业地图 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_09(self):
        '''首页跳转创新主体页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[5]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('创新主体 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_10(self):
        '''首页跳转创新成果页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[5]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('创新成果 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_11(self):
        '''首页跳转产业链图谱页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[1]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('产业链图谱 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_12(self):
        '''首页跳转招商图谱页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[2]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('招商图谱 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_13(self):
        '''首页跳转资本流动页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[2]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('资本流动 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_14(self):
        '''首页跳转开发发展-结构分析页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[3]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('结构分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_15(self):
        '''首页跳转地域分析页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[3]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('地域分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_16(self):
        '''首页跳转企业分析页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[3]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[3]/a/li/span')
            time.sleep(1)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('企业分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_17(self):
        '''首页跳转总体概览页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[4]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(2)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('总体概览 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_18(self):
        '''首页跳转结构分析页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[4]/li/div/span')
            time.sleep(1)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(2)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('结构分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
    def test_19(self):
        '''切换城市'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[10]/span')
            time.sleep(3)
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        Sftext = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '// *[ @ id = "leftTopChart"] / div[1] / p[2] / small / span')
        self.assertEqual('河南省', Sftext, '用例执行错误')
        Sftext2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
        self.assertEqual('郑州市', Sftext2, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
