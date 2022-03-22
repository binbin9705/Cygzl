import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo
import warnings


# @unittest.skip('调试')
class Test02(unittest.TestCase):
    '''切换地区'''

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
        # pass

    def setUp(self):
        # # 启动浏览并设置相关选项
        # self.driver = webdriver.Chrome(options=WebGetDemo.Runmian(self).options())
        self.imgs = []
        # WebGetDemo.Runmian(self.driver).open('http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard')
        # WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')
        # pass
        self.driver.implicitly_wait(5)

    def add_img(self):
        # 1、下面注释掉的这行代码作用是不管用例是否执行成功，只要在执行过程加了self.add_img()操作，那么最后生成的报告中含有该执行过程的截图，如果不添加则默认对用例失败进行截图
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def tearDown(self):
        self.driver.refresh()

    def test_01(self):
        '''切换地区-热门城市：上海市'''
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[5]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/button/span')
            self.assertEqual('上海市', ys, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_02(self):
        '''切换地区-热门城市：杭州市'''
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[8]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/button/span')
            t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
            t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
            self.assertEqual('杭州市', ys, '用例执行错误')
            self.assertEqual('浙江省', t1, '用例执行错误')
            self.assertEqual('浙江省', t2, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_03(self):
        '''切换地区-按省份快捷查看-B'''
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/button')
            time.sleep(3)
            # 点击按省份下的B
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[2]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div/div[1]')
            self.assertEqual('110000', adcode, '用例执行错误')
            self.assertEqual('北京市', title, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_04(self):
        '''切换地区-按城市快捷查看-F'''
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/button')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[6]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[6]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
