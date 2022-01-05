import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo
import warnings


# @unittest.skip('调试')
class Test3(unittest.TestCase):
    '''首页页面交互-按城市切换地区'''

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
        '''切换地区-按城市快捷查看-A'''
        self.driver.implicitly_wait(5)
        try:
            # 点击右上角地区切换按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            # 点击按城市
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            # 点击A
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[1]')
            time.sleep(2)
            # 获取A的class状态
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[1]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_02(self):
        '''切换地区-按城市快捷查看-B'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[2]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[2]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_03(self):
        '''切换地区-按城市快捷查看-C'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[3]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[3]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_04(self):
        '''切换地区-按城市快捷查看-D'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[4]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[4]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_05(self):
        '''切换地区-按城市快捷查看-E'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[5]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[5]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_06(self):
        '''切换地区-按城市快捷查看-F'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
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

    def test_07(self):
        '''切换地区-按城市快捷查看-G'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[7]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[7]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_08(self):
        '''切换地区-按城市快捷查看-H'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[8]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[8]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_09(self):
        '''切换地区-按城市快捷查看-J'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[9]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[9]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_10(self):
        '''切换地区-按城市快捷查看-K'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[10]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[10]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_11(self):
        '''切换地区-按城市快捷查看-L'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[11]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[11]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_12(self):
        '''切换地区-按城市快捷查看-M'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[12]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[12]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_13(self):
        '''切换地区-按城市快捷查看-N'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[13]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[13]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_14(self):
        '''切换地区-按城市快捷查看-P'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[14]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[14]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_15(self):
        '''切换地区-按城市快捷查看-Q'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[15]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[15]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_16(self):
        '''切换地区-按城市快捷查看-S'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[16]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[16]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_17(self):
        '''切换地区-按城市快捷查看-T'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[17]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[17]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_18(self):
        '''切换地区-按城市快捷查看-W'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[18]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[18]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_19(self):
        '''切换地区-按城市快捷查看-X'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[19]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[19]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_20(self):
        '''切换地区-按城市快捷查看-Y'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[20]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[20]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise

    def test_21(self):
        '''切换地区-按城市快捷查看-Z'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[21]')
            time.sleep(2)
            classvlue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[21]')
            self.assertEqual('active', classvlue, '用例执行错误')
        except Exception:
            self.add_img()
            raise


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
