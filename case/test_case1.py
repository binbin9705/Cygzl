import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo
import warnings


# @unittest.skip('调试')
class Test1(unittest.TestCase):
    '''页面跳转'''

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
        '''首页跳转CRL指数页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[2]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(2)
            self.assertEqual('CRI指数 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_02(self):
        '''首页跳转企业总量页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[2]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            # 判断跳转后的标签页是不是企业总量
            self.assertEqual('企业总量 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_03(self):
        '''首页跳转行业分析页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[2]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[3]/a/li/span')
            time.sleep(2)
            self.assertEqual('行业分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_04(self):
        '''首页跳转结构分析页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[2]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[4]/a/li/span')
            time.sleep(2)
            self.assertEqual('结构分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_05(self):
        '''首页跳转重点企业页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[2]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[5]/a/li/span')
            time.sleep(2)
            self.assertEqual('重点企业 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_06(self):
        '''首页跳转总体监测页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[3]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(2)
            self.assertEqual('总体监测 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_07(self):
        '''首页跳转产业分析页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[3]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(2)
            self.assertEqual('产业分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_08(self):
        '''首页跳转产业地图页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[4]/a/li/span')
            time.sleep(2)
            self.assertEqual('产业地图 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_09(self):
        '''首页跳转创新主体页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[5]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(2)
            self.assertEqual('创新主体 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_10(self):
        '''首页跳转创新成果页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[5]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(2)
            self.assertEqual('创新成果 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_11(self):
        '''首页跳转产业链图谱页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[1]/a/li/span')
            time.sleep(2)
            self.assertEqual('产业链图谱 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_12(self):
        '''首页跳转招商图谱页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[2]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(2)
            self.assertEqual('招商图谱 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_13(self):
        '''首页跳转资本流动页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[2]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(2)
            self.assertEqual('资本流动 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_14(self):
        '''首页跳转开发发展-结构分析页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[3]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(2)
            self.assertEqual('结构分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_15(self):
        '''首页跳转地域分析页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[3]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(2)
            self.assertEqual('地域分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_16(self):
        '''首页跳转企业分析页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[3]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[3]/a/li/span')
            time.sleep(2)
            self.assertEqual('企业分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_17(self):
        '''首页跳转总体概览页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[4]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(2)
            self.assertEqual('总体概览 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_18(self):
        '''首页跳转结构分析页面'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[4]/li/div/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(2)
            self.assertEqual('结构分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        except Exception:
            self.add_img()
            raise


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
