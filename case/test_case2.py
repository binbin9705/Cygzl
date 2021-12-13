import unittest
import time
from selenium import webdriver
from PublicMethod import WebGetDemo
import warnings


class Test2(unittest.TestCase):
    '''首页页面交互'''

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
        WebGetDemo.Runmian(self.driver).open(login_url)
        WebGetDemo.Runmian(self.driver).login(name, password)

    def tearDown(self):
        WebGetDemo.Runmian(self.driver).quit()

    #@unittest.skip('跳过')
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

    #@unittest.skip('跳过')
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

    #@unittest.skip('跳过')
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

        #@unittest.skip('跳过')
        def test_04(self):
            '''切换地区-沈阳市'''
            self.driver.implicitly_wait(5)
            try:
                WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
                time.sleep(3)
                WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[3]/span')
                time.sleep(3)
                ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
                t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                                '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
                t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                                '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
            except AssertionError as e:
                # 调用封装好的截图方法，进行截图并保存在本地磁盘
                WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
            except Exception as e:
                WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
            self.assertEqual('沈阳市', ys, '用例执行错误')
            self.assertEqual('辽宁省', t1, '用例执行错误')
            self.assertEqual('辽宁省', t2, '用例执行错误')

    #@unittest.skip('跳过')
    def test_05(self):
        '''切换地区-大连市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[4]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
            t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
            t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('大连市', ys, '用例执行错误')
        self.assertEqual('辽宁省', t1, '用例执行错误')
        self.assertEqual('辽宁省', t2, '用例执行错误')

    #@unittest.skip('跳过')
    def test_06(self):
        '''切换地区-上海市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[5]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('上海市', ys, '用例执行错误')

    #@unittest.skip('跳过')
    def test_07(self):
        '''切换地区-南京市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[6]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
            t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
            t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('南京市', ys, '用例执行错误')
        self.assertEqual('江苏省', t1, '用例执行错误')
        self.assertEqual('江苏省', t2, '用例执行错误')

    #@unittest.skip('跳过')
    def test_08(self):
        '''切换地区-苏州市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[7]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
            t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
            t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)

        self.assertEqual('苏州市', ys, '用例执行错误')
        self.assertEqual('江苏省', t1, '用例执行错误')
        self.assertEqual('江苏省', t2, '用例执行错误')

    #@unittest.skip('跳过')
    def test_09(self):
        '''切换地区-杭州市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[8]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
            t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
            t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('杭州市', ys, '用例执行错误')
        self.assertEqual('浙江省', t1, '用例执行错误')
        self.assertEqual('浙江省', t2, '用例执行错误')

    #@unittest.skip('跳过')
    def test_10(self):
        '''切换地区-青岛市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[9]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
            t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
            t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('青岛市', ys, '用例执行错误')
        self.assertEqual('山东省', t1, '用例执行错误')
        self.assertEqual('山东省', t2, '用例执行错误')

    #@unittest.skip('跳过')
    def test_11(self):
        '''切换地区-郑州市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[10]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
            t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
            t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('郑州市', ys, '用例执行错误')
        self.assertEqual('河南省', t1, '用例执行错误')
        self.assertEqual('河南省', t2, '用例执行错误')

    #@unittest.skip('跳过')
    def test_12(self):
        '''切换地区-武汉市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[11]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
            t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
            t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('武汉市', ys, '用例执行错误')
        self.assertEqual('湖北省', t1, '用例执行错误')
        self.assertEqual('湖北省', t2, '用例执行错误')

    #@unittest.skip('跳过')
    def test_13(self):
        '''切换地区-长沙市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[12]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
            t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
            t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('长沙市', ys, '用例执行错误')
        self.assertEqual('湖南省', t1, '用例执行错误')
        self.assertEqual('湖南省', t2, '用例执行错误')

    #@unittest.skip('跳过')
    def test_14(self):
        '''切换地区-广州市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[13]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
            t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
            t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('广州市', ys, '用例执行错误')
        self.assertEqual('广东省', t1, '用例执行错误')
        self.assertEqual('广东省', t2, '用例执行错误')

    #@unittest.skip('跳过')
    def test_15(self):
        '''切换地区-深圳市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[14]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
            t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
            t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('深圳市', ys, '用例执行错误')
        self.assertEqual('广东省', t1, '用例执行错误')
        self.assertEqual('广东省', t2, '用例执行错误')

    #@unittest.skip('跳过')
    def test_16(self):
        '''切换地区-重庆市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[15]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('重庆市', ys, '用例执行错误')

    #@unittest.skip('跳过')
    def test_17(self):
        '''切换地区-成都市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[16]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
            t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
            t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('成都市', ys, '用例执行错误')
        self.assertEqual('四川省', t1, '用例执行错误')
        self.assertEqual('四川省', t2, '用例执行错误')

    #@unittest.skip('跳过')
    def test_18(self):
        '''切换地区-西安市'''
        self.driver.implicitly_wait(5)
        try:
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="tip"]/div/ul/span[17]/span')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="placePop"]/span/button/span')
            t1 = WebGetDemo.Runmian(self.driver).obtaintest('xpath', '//*[@id="leftTopChart"]/div[1]/p[2]/small/span')
            t2 = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                            '//*[@id="bottomLeftChart"]/div[1]/p[1]/small[2]/span')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('西安市', ys, '用例执行错误')
        self.assertEqual('陕西省', t1, '用例执行错误')
        self.assertEqual('陕西省', t2, '用例执行错误')

    #@unittest.skip('跳过')
    def test_19(self):
        '''切换地区-按省份快捷查看-A'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的A
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[1]')
            time.sleep(3)
            ys = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                             '//*[@id="tip"]/div/section/ul/div/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('安徽省', ys, '用例执行错误')

    #@unittest.skip('跳过')
    def test_20(self):
        '''切换地区-按省份快捷查看-B'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的B
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[2]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('110000', adcode, '用例执行错误')
        self.assertEqual('北京市', title, '用例执行错误')

    #@unittest.skip('跳过')
    def test_21(self):
        '''切换地区-按省份快捷查看-C'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的C
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[3]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('500000', adcode, '用例执行错误')
        self.assertEqual('重庆市', title, '用例执行错误')

    #@unittest.skip('跳过')
    def test_22(self):
        '''切换地区-按省份快捷查看-F'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的F
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[4]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('350000', adcode, '用例执行错误')
        self.assertEqual('福建省', title, '用例执行错误')

    #@unittest.skip('跳过')
    def test_23(self):
        '''切换地区-按省份快捷查看-G'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的G
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[5]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('440000', adcode, '用例执行错误')
        self.assertEqual('广东省', title, '用例执行错误')

    #@unittest.skip('跳过')
    def test_24(self):
        '''切换地区-按省份快捷查看-H'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的H
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[6]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('130000', adcode, '用例执行错误')
        self.assertEqual('河北省', title, '用例执行错误')

    #@unittest.skip('跳过')
    def test_25(self):
        '''切换地区-按省份快捷查看-J'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的J
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[7]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div[1]/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div[1]/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('220000', adcode, '用例执行错误')
        self.assertEqual('吉林省', title, '用例执行错误')

    #@unittest.skip('跳过')
    def test_26(self):
        '''切换地区-按省份快捷查看-L'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的L
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[8]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('210000', adcode, '用例执行错误')
        self.assertEqual('辽宁省', title, '用例执行错误')

    #@unittest.skip('跳过')
    def test_27(self):
        '''切换地区-按省份快捷查看-N'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的N
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[9]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('150000', adcode, '用例执行错误')
        self.assertEqual('内蒙古自治区', title, '用例执行错误')

    #@unittest.skip('跳过')
    def test_28(self):
        '''切换地区-按省份快捷查看-Q'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的Q
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[10]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('630000', adcode, '用例执行错误')
        self.assertEqual('青海省', title, '用例执行错误')

    #@unittest.skip('跳过')
    def test_29(self):
        '''切换地区-按省份快捷查看-S'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的S
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[11]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div[1]/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div[1]/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('140000', adcode, '用例执行错误')
        self.assertEqual('山西省', title, '用例执行错误')

    #@unittest.skip('跳过')
    def test_30(self):
        '''切换地区-按省份快捷查看-T'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的T
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[12]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('120000', adcode, '用例执行错误')
        self.assertEqual('天津市', title, '用例执行错误')

    #@unittest.skip('跳过')
    def test_31(self):
        '''切换地区-按省份快捷查看-X'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的X
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[13]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div[1]/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div[1]/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('540000', adcode, '用例执行错误')
        self.assertEqual('西藏自治区', title, '用例执行错误')

    #@unittest.skip('跳过')
    def test_32(self):
        '''切换地区-按省份快捷查看-Y'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的Y
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[14]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('530000', adcode, '用例执行错误')
        self.assertEqual('云南省', title, '用例执行错误')

    #@unittest.skip('跳过')
    def test_33(self):
        '''切换地区-按省份快捷查看-Z'''
        self.driver.implicitly_wait(5)
        try:
            # 点击切换地区按钮
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="placePop"]/span/button/span')
            time.sleep(3)
            # 点击按省份下的Z
            WebGetDemo.Runmian(self.driver).click('xpath', '//*[@id="cityListT"]/span[15]')
            time.sleep(3)
            adcode = WebGetDemo.Runmian(self.driver).obtainvalue('adcode', 'xpath',
                                                                 '//*[@id="tip"]/div/section/ul/div/div[1]')
            title = WebGetDemo.Runmian(self.driver).obtainvalue('title', 'xpath',
                                                                '//*[@id="tip"]/div/section/ul/div/div[1]')
        except AssertionError as e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        except Exception as e:
            WebGetDemo.Runmian(self.driver).takeScreenshot(WebGetDemo.Runmian(self.driver).createDir(), e)
        self.assertEqual('330000', adcode, '用例执行错误')
        self.assertEqual('浙江省', title, '用例执行错误')


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
