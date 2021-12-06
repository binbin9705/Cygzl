import traceback
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from PublicMethod import WebGetDemo
import warnings


class Test1(unittest.TestCase):

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
        WebGetDemo.Runmian(self.driver).open('http://ihd.wanvdata.cn/')

    def tearDown(self):
        pass

    @unittest.skip('调试')
    def test_01(self):
        '''首页跳转CRL指数页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[2]/li/div/span')
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

    @unittest.skip('跳过')
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

    @unittest.skip('跳过')
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

    @unittest.skip('跳过')
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

    @unittest.skip('跳过')
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

    @unittest.skip('跳过')
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

    @unittest.skip('跳过')
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

    @unittest.skip('跳过')
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

    @unittest.skip('跳过')
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

    @unittest.skip('跳过')
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

    @unittest.skip('跳过')
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

    @unittest.skip('跳过')
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
    @unittest.skip('跳过')
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
if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
