import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PublicMethod import WebGetDemo
from selenium.webdriver.common.by import By
import warnings
import random


# @unittest.skip('调试')
class Test09(unittest.TestCase):
    '''招商引资'''

    @classmethod
    def setUpClass(cls):
        # 启动浏览并设置相关选项
        cls.driver = webdriver.Chrome(options=WebGetDemo.Runmian(cls).options())
        # cls.imgs = []
        WebGetDemo.Runmian(cls.driver).open('http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard')
        WebGetDemo.Runmian(cls.driver).login(username='ihqd-test', password='ihqd-test@6688')
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
        self.driver.refresh()
        self.driver.implicitly_wait(5)

    def add_img(self):
        # 1、下面注释掉的这行代码作用是不管用例是否执行成功，只要在执行过程加了self.add_img()操作，那么最后生成的报告中含有该执行过程的截图，如果不添加则默认对用例失败进行截图
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def tearDown(self):
        # WebGetDemo.Runmian(self.driver).quit()
        pass

    def test_01(self):
        '''招商引资-招商图谱-切换产业'''
        try:
            time.sleep(3)
            # 点击招商引资
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header/div[1]/ul/div[3]/div[2]/li/div[1]/i')
            time.sleep(3)
            # 点击招商图谱
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(3)
            # 点击产业下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/span/span/i')
            time.sleep(3)
            # 选择新材料
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')
            time.sleep(2)
            # 获取新材料的class值
            classvalue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'xpath',
                                                                     '/html/body/div[3]/div[1]/div[1]/ul/li[2]')
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_02(self):
        '''招商引资-招商图谱-收起图谱'''
        try:
            # time.sleep(3)
            # # 点击招商引资
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[2]/li/div/i')
            # time.sleep(3)
            # # 点击招商图谱
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(3)
            # 点击产业下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/span/span/i')
            time.sleep(3)
            # 选择新材料
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[2]/span')
            time.sleep(2)
            # 点击收起图谱
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/div/div[3]/button')
            time.sleep(2)
            # 获取按钮的文本值
            textvalue = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                                   '//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/div/div[3]/button/span')
            self.assertEqual('展开图谱', textvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_03(self):
        '''招商引资-招商图谱-随机跳转分页后随机跳转企业详情'''
        try:
            # time.sleep(3)
            # # 点击招商引资
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[2]/li/div/i')
            # time.sleep(3)
            # # 点击招商图谱
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(3)
            # 点击产业下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/span/span/i')
            time.sleep(3)
            # 选择新材料
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[2]/span')
            time.sleep(2)
            # 点击收起图谱
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/div/div[3]/button')
            time.sleep(2)
            # 移动到浏览器低部
            js = 'document.querySelector("html").scrollTop=10000'
            self.driver.execute_script(js)
            time.sleep(2)
            # 随机切换分页
            num = random.randint(2, 6)
            js2 = 'document.querySelector("#app > div > div > section > div > div:nth-child(2) > div > div.el-tabs__content > div > div.ent-list-pages > div > ul > li:nth-child(' + str(
                num) + ')").click()'
            self.driver.execute_script(js2)
            time.sleep(3)
            # 切换到浏览器顶部
            js3 = 'document.querySelector("html").scrollTop=0'
            self.driver.execute_script(js3)
            time.sleep(3)
            # 随机跳转一家企业详情
            # 获取跳转企业的名称
            num2 = random.randint(2, 4)
            js4 = 'return document.querySelector("#app > div > div > section > div > div:nth-child(2) > div > div.el-tabs__content > div > div.ent-box > div:nth-child(' + str(
                num2) + ') > div.ent-left > h3").innerText'
            textvalue = self.driver.execute_script(js4)
            # 随机跳转一家企业详情
            js5 = 'document.querySelector("#app > div > div > section > div > div:nth-child(2) > div > div.el-tabs__content > div > div.ent-box > div:nth-child(' + str(
                num2) + ') > div.ent-left > h3").click()'
            self.driver.execute_script(js5)
            time.sleep(3)
            # 切换到新title页
            WebGetDemo.Runmian(self.driver).switch_window_by_title('企业大数据')
            # 切换到新的frame里
            WebGetDemo.Runmian(self.driver).switch_window_by_frame('com_frame')
            time.sleep(3)
            newtextvalue = WebGetDemo.Runmian(self.driver).obtaintest('class_name', 'p_entName')
            self.assertEqual(textvalue, newtextvalue, '用例执行错误')
            WebGetDemo.Runmian(self.driver).switch_window_by_title('招商图谱 - 产业高质量发展平台')
            time.sleep(2)
        except Exception:
            self.add_img()
            raise

    def test_04(self):
        '''招商引资-招商图谱-随机跳转分页后随机跳转招商路径或族谱'''
        try:
            # time.sleep(3)
            # # 点击招商引资
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[2]/li/div/i')
            # time.sleep(3)
            # # 点击招商图谱
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[1]/a/li/span')
            time.sleep(3)
            # 点击产业下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/div/div[1]/div/div[1]/span/span/i')
            time.sleep(3)
            # 选择新材料
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[2]/span')
            time.sleep(2)
            # 点击收起图谱
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/div/div[3]/button')
            time.sleep(2)
            # 移动到浏览器低部
            js = 'document.querySelector("html").scrollTop=0'
            self.driver.execute_script(js)
            time.sleep(2)
            # 随机跳转企业族谱或招商路径
            num = random.randint(2, 7)
            js2 = 'document.getElementsByClassName("el-button")[' + str(num) + '].click()'
            self.driver.execute_script(js2)
            time.sleep(3)
            # 切换到新title页
            WebGetDemo.Runmian(self.driver).switch_window_by_title('企业大数据')
            self.assertEqual('企业大数据', self.driver.title, '用例执行错误')
            WebGetDemo.Runmian(self.driver).switch_window_by_title('招商图谱 - 产业高质量发展平台')
            time.sleep(2)
        except Exception:
            self.add_img()
            raise

    def test_05(self):
        '''招商引资-流动资本-随机切换年份'''
        try:
            time.sleep(3)
            # 点击招商引资
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header/div[1]/ul/div[3]/div[2]/li/div[1]/i')
            time.sleep(3)
            # 点击流动资本
            WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(3)
            # 点击统计年份下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/div/div[1]/div[1]/div/span/span/i')
            time.sleep(3)
            # 随机选择一个年份
            num = random.randint(1, 4)
            js = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(3)
            js2 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js2)
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_06(self):
        '''招商引资-流动资本-切换市'''
        try:
            # time.sleep(3)
            # # 点击招商引资
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[2]/li/div/i')
            # time.sleep(3)
            # # 点击流动资本
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(3)
            # 点击统计图中的市
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/div/div[1]/div[3]/small[2]')
            time.sleep(2)
            # 获取市的class
            js = 'return document.querySelector("#app > div > div > section > div > div:nth-child(2) > div > div.el-tabs__content > div > div.invest-control > div.invest-tab > small.active").getAttribute("class")'
            classvalue = self.driver.execute_script(js)
            self.assertIn('active', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_07(self):
        '''招商引资-流动资本-切换对外投资'''
        try:
            # time.sleep(3)
            # # 点击招商引资
            # WebGetDemo.Runmian(self.driver).click('xpath',
            #                                       '//*[@id="app"]/div/header[2]/div[1]/ul/div[3]/div[2]/li/div/i')
            # time.sleep(3)
            # # 点击流动资本
            # WebGetDemo.Runmian(self.driver).click('xpath', '/html/body/div[2]/ul/div[2]/a/li/span')
            time.sleep(3)
            # 点击对外投资
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/div/div[1]/div[2]/label[2]/span')
            time.sleep(2)
            # 获取对外投资的class
            js = 'return document.querySelector("#app > div > div > section > div > div:nth-child(2) > div > div.el-tabs__content > div > div.invest-control > div.el-radio-group.gradient > label.el-radio-button.is-active").getAttribute("class")'
            classvalue = self.driver.execute_script(js)
            self.assertIn('is-active', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
