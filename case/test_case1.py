import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo
import warnings
class Test1(unittest.TestCase):
    @classmethod
    #123
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
    # @unittest.skip('调试')
    def test_01(self):
        '''首页跳转CRL指数页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath','//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[2]/li/div/span')
            time.sleep(1)
        except:
            #如果发生错误截图当前页面
            WebGetDemo.Runmian(self.driver).jietu("D:\pycharm\Jjdn\error_png\\test_01\error01.png")
        try:
            WebGetDemo.Runmian(self.driver).click('xpath','/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(1)
        except:
            WebGetDemo.Runmian(self.driver).jietu("D:\pycharm\Jjdn\error_png\\test_01\error02.png")
        print(self.driver.title)
        time.sleep(1)
        self.assertEqual('CRI指数 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()
    # @unittest.skip('跳过')
    def test_02(self):
        '''首页跳转企业总量页面'''
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        try:
            WebGetDemo.Runmian(self.driver).click('xpath','//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[2]/li/div/span')
            time.sleep(1)
        except:
            #如果发生错误截图当前页面
            WebGetDemo.Runmian(self.driver).jietu("D:\pycharm\Jjdn\error_png\\test_02\error01.png")
        #
        try:
            WebGetDemo.Runmian(self.driver).click('xpath','/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(1)
        except:
            WebGetDemo.Runmian(self.driver).jietu("D:\pycharm\Jjdn\error_png\\test_02\error02.png")

        print(self.driver.title)
        time.sleep(1)
        self.assertEqual('企业总量 - 产业高质量发展平台', self.driver.title, '用例执行错误')
        WebGetDemo.Runmian(self.driver).quit()
if __name__ == '__main__':
    login_url='http://ihd.wanvdata.cn/'
    name='ihqd-test'
    password='ihqd-test@6688'
    unittest.main(verbosity=2)
