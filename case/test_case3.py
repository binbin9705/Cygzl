import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo
import warnings

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
        # self.driver.maximize_window()
        WebGetDemo.Runmian(self.driver).open('http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard')
        time.sleep(2)
        WebGetDemo.Runmian(self.driver).login('ihqd-test', 'ihqd-test@6688')

    def tearDown(self):
        WebGetDemo.Runmian(self.driver).quit()
    #@unittest.skip('跳过')
    def test_01(self):
        '''切换地区-按城市快捷查看-A'''
        self.driver.implicitly_wait(5)
        try:
            #点击右上角地区切换按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(2)
            #点击按城市
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListType"]/div[1]/label[2]')
            time.sleep(2)
            #点击A
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListTP"]/span[1]')
            time.sleep(2)
            #获取A的class状态
            classvlue=WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active',classvlue,'用例执行错误')

    #@unittest.skip('跳过')
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
            classvlue=WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[2]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active',classvlue,'用例执行错误')

    #@unittest.skip('跳过')
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
            classvlue=WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath', '//*[@id="cityListTP"]/span[3]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active',classvlue,'用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')

    #@unittest.skip('跳过')
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
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('active', classvlue, '用例执行错误')



if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
