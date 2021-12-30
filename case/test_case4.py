import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo
import warnings

# @unittest.skip('调试')
class Test4(unittest.TestCase):
    '''首页页面交互-统计图交互、搜索企业'''

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

    def test_01(self):
        '''市场主体统计图切换统计条件-高薪企业'''
        self.driver.implicitly_wait(5)
        try:
            time.sleep(3)
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

    def test_02(self):
        '''市场主体统计图切换统计条件-战兴企业'''
        self.driver.implicitly_wait(5)
        try:
            time.sleep(3)
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
        self.assertNotEqual(classvalue, afterclassvalue, '用例执行错误')

    def test_03(self):
        '''左上角搜索-输入内容为华为'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[1]/input')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).input_data('xpath',
                                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[1]/input',
                                                       '华为')
            time.sleep(3)
            test = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                              '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[2]/div[1]/div[1]/ul/li[1]/span')
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[2]/div[1]/div[1]/ul/li[1]/span')
            time.sleep(3)
            # 切换到新title页
            WebGetDemo.Runmian(self.driver).switch_window_by_title('企业大数据')
            # 切换到新的frame里
            WebGetDemo.Runmian(self.driver).switch_window_by_frame('com_frame')
            newtest = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                                 '//*[@id="mapMainBox"]/body/div[3]/div[1]/div[1]/div[2]/h3')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        # 判断跳转后的页面数据=搜索联想下拉框的第一条数据就通过
        self.assertEqual(test, newtest, '用例执行失败，跳转页面错误')

    def test_04(self):
        '''左上角搜索-输入内容为123456'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[1]/input')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).input_data('xpath',
                                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[1]/input',
                                                       '123456')
            time.sleep(2)
            # 获取搜索联想下拉框的第一条数据名称
            test = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                              '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[2]/p')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        # 断言如果等于无数据cas就通过
        self.assertEqual(test, '无数据', '用例执行失败')

    def test_05(self):
        '''左上角搜索-输入内容字节长度为1'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[1]/input')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).input_data('xpath',
                                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[1]/input',
                                                       '1')
            time.sleep(3)
            # 获取搜索联想下拉框的第一条数据名称
            test = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                              '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[2]/p')
            errortest = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   'body > div.el-message.el-message--error > p')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        # 断言如果等于无数据case就通过
        self.assertEqual(test, '无数据', '用例执行失败')
        # 断言字符串是否包含在警告框中如果在就不通过
        self.assertNotIn('接口请求失败', errortest, '接口正常报错输入内容字节长度为1位')


    def test_06(self):
        '''左上角搜索-输入内容为地区名称：北京'''
        self.driver.implicitly_wait(5)
        try:
            # 点击搜索输入文本框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[1]/input')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).input_data('xpath',
                                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[1]/input',
                                                       '北京')
            time.sleep(2)
            # 获取搜索联想下拉框的第一条数据名称
            test = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                              '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[2]/p')
            # 获取警告框中的test
            errortest = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   'body > div.el-message.el-message--error > p')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        # 断言如果等于无数据case就通过
        self.assertEqual(test, '无数据', '用例执行失败')
        # 断言字符串是否包含在警告框中如果在就不通过
        self.assertNotIn('接口请求失败',errortest, '接口正常报错输入内容为地区名称时报错')

    # @unittest.skip('跳过')
    def test_07(self):
        '''左上角搜索-输入内容为：~！'''
        self.driver.implicitly_wait(5)
        try:
            # 点击搜索输入文本框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[1]/input')
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).input_data('xpath',
                                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[1]/input',
                                                       '~！')
            time.sleep(2)
            # 获取搜索联想下拉框的第一条数据名称
            test = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                              '//*[@id="app"]/div/header[2]/div[1]/ul/div[1]/div[1]/div[2]/p')
            # 获取警告框中的test
            errortest = WebGetDemo.Runmian(self.driver).obtaintest('css',
                                                                   'body > div.el-message.el-message--error > p')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        # 断言如果等于无数据case就通过
        self.assertEqual(test, '无数据', '用例执行失败')
        # 断言字符串是否包含在警告框中如果在就不通过
        self.assertNotIn('接口请求失败',errortest, '接口正常报错输入内容字节长度为1位以上的任意特殊字符')

if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
