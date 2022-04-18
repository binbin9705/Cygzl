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
class Test08(unittest.TestCase):
    '''产业链图谱'''

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
        self.driver.implicitly_wait(5)

    def add_img(self):
        # 1、下面注释掉的这行代码作用是不管用例是否执行成功，只要在执行过程加了self.add_img()操作，那么最后生成的报告中含有该执行过程的截图，如果不添加则默认对用例失败进行截图
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def tearDown(self):
        self.driver.refresh()

    def test_01(self):
        '''产业链图谱-切换现状图'''
        try:
            time.sleep(3)
            # 点击产业链图谱
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="app"]/div/header/div[1]/ul/div[3]/div[1]/a/li/span')
            time.sleep(3)
            # 点击现状图
            WebGetDemo.Runmian(self.driver).click('id', 'tab-xzt')
            time.sleep(2)
            # 获取现状图的class值
            classvalue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'id', 'tab-xzt')
            self.assertIn('is-active', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_02(self):
        '''产业链图谱-切换分布图'''
        try:
            # time.sleep(3)
            # # 点击产业链图谱
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-right > div:nth-child(1) > a > li')
            # time.sleep(3)
            # 点击分布图
            WebGetDemo.Runmian(self.driver).click('id', 'tab-fbt')
            time.sleep(2)
            # 获取现状图的class值
            classvalue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'id', 'tab-fbt')
            self.assertIn('is-active', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_03(self):
        '''产业链图谱-全景图-切换行业'''
        try:
            # time.sleep(3)
            # # 点击产业链图谱
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-right > div:nth-child(1) > a > li')
            time.sleep(3)
            # 点击行业下拉框
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="pane-qjt"]/div/div[1]/div/div[1]/span/span/i')
            time.sleep(2)
            # 选择新材料
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')
            time.sleep(2)
            # 获取新材料的class值
            classvalue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                     'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_04(self):
        '''产业链图谱-现状图-切换行业'''
        try:
            # time.sleep(3)
            # # 点击产业链图谱
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-right > div:nth-child(1) > a > li')
            time.sleep(3)
            # 点击现状图
            WebGetDemo.Runmian(self.driver).click('id', 'tab-xzt')
            time.sleep(2)
            # 点击行业下拉框
            WebGetDemo.Runmian(self.driver).click('css', '#pane-xzt > div > div.control > div > div > span > span > i')
            time.sleep(2)
            # 选择新材料
            WebGetDemo.Runmian(self.driver).click('css',
                                                  'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')
            time.sleep(2)
            # 获取新材料的class值
            classvalue = WebGetDemo.Runmian(self.driver).obtainvalue('class', 'css',
                                                                     'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)')
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_05(self):
        '''产业链图谱-现状图-企业列表随机翻页随机跳转企业详情'''
        try:
            # time.sleep(3)
            # # 点击产业链图谱
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-right > div:nth-child(1) > a > li')
            time.sleep(3)
            # 点击现状图
            WebGetDemo.Runmian(self.driver).click('id', 'tab-xzt')
            time.sleep(3)
            # 移动至浏览器底部
            js = 'document.querySelector("html").scrollTop=10000'
            self.driver.execute_script(js)
            time.sleep(2)
            # 企业列表随机翻页
            num = random.randint(1, 6)
            js = 'document.getElementsByClassName("number")[' + str(num) + '].click()'
            self.driver.execute_script(js)
            time.sleep(2)
            num2 = random.randint(1, 20)
            # 获取要跳转的企业名称
            testvalue = WebGetDemo.Runmian(self.driver).obtaintest('xpath',
                                                                   '//*[@id="pane-xzt"]/div/div[4]/div/div[1]/div[1]/div[3]/table/tbody/tr[' + str(
                                                                       num2) + ']/td[2]/div/p')
            # 随机跳转一家企业详情
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="pane-xzt"]/div/div[4]/div/div[1]/div[1]/div[3]/table/tbody/tr[' + str(
                                                      num2) + ']/td[2]/div/p')
            time.sleep(3)
            # 切换到新title页
            WebGetDemo.Runmian(self.driver).switch_window_by_title('企业大数据')
            # 切换到新的frame里
            WebGetDemo.Runmian(self.driver).switch_window_by_frame('com_frame')
            time.sleep(3)
            # 获取企业详情中的企业名称
            newqytest = WebGetDemo.Runmian(self.driver).obtaintest('class_name', 'p_entName')
            time.sleep(3)
            self.assertEqual(newqytest, testvalue, '用例执行错误')
            WebGetDemo.Runmian(self.driver).switch_window_by_title('产业链图谱 - 产业高质量发展平台')
            time.sleep(2)
        except Exception:
            self.add_img()
            raise

    def test_06(self):
        '''产业链图谱-现状图-企业列表随机切换分页条数'''
        try:
            # time.sleep(3)
            # # 点击产业链图谱
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-right > div:nth-child(1) > a > li')
            time.sleep(3)
            # 点击现状图
            WebGetDemo.Runmian(self.driver).click('id', 'tab-xzt')
            time.sleep(3)
            # 移动至浏览器底部
            js = 'document.querySelector("html").scrollTop=10000'
            self.driver.execute_script(js)
            time.sleep(2)
            # 随机切换50/100条一页
            WebGetDemo.Runmian(self.driver).click('xpath',
                                                  '//*[@id="pane-xzt"]/div/div[4]/div/div[2]/div/span[2]/div/div/span/span/i')
            time.sleep(2)
            num = random.randint(3, 4)
            js2 = 'document.getElementsByClassName("el-select-dropdown__item")[' + str(num) + '].click()'
            self.driver.execute_script(js2)
            time.sleep(2)
            js3 = 'return document.getElementsByClassName("el-select-dropdown__item")[' + str(
                num) + '].getAttribute("class")'
            classvalue = self.driver.execute_script(js3)
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_07(self):
        '''产业链图谱-现状图-企业列表快捷跳转分页'''
        try:
            # time.sleep(3)
            # # 点击产业链图谱
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-right > div:nth-child(1) > a > li')
            time.sleep(3)
            # 点击现状图
            WebGetDemo.Runmian(self.driver).click('id', 'tab-xzt')
            time.sleep(3)
            # 移动至浏览器底部
            js = 'document.querySelector("html").scrollTop=10000'
            self.driver.execute_script(js)
            # 随机输入页数
            num = random.randint(1, 20)
            time.sleep(2)
            # 删除当前页码
            self.driver.find_element(By.XPATH,
                                     '//*[@id="pane-xzt"]/div/div[4]/div/div[2]/div/span[3]/div/input').send_keys(
                Keys.BACK_SPACE)
            time.sleep(2)
            WebGetDemo.Runmian(self.driver).input_data('xpath',
                                                       '//*[@id="pane-xzt"]/div/div[4]/div/div[2]/div/span[3]/div/input',
                                                       num)
            time.sleep(2)
            # 调用回车
            self.driver.find_element(By.XPATH,
                                     '//*[@id="pane-xzt"]/div/div[4]/div/div[2]/div/span[3]/div/input').send_keys(
                Keys.ENTER)
            time.sleep(2)
            # 获取跳转页码的文本值
            js2 = 'return document.querySelector("#pane-xzt > div > div.ent-box > div > div.pageControl > div > ul > li.number.active").innerText'
            textvalue = self.driver.execute_script(js2)
            self.assertEqual(textvalue, str(num), '用例执行失败')
        except Exception:
            self.add_img()
            raise

    def test_08(self):
        '''产业链图谱-分布图-切换产业'''
        try:
            # time.sleep(3)
            # # 点击产业链图谱
            # WebGetDemo.Runmian(self.driver).click('css',
            #                                       '#app > div > header.layout-header-fixed > div.header > ul > div.header-right > div:nth-child(1) > a > li')
            time.sleep(3)
            # 点击分布图
            WebGetDemo.Runmian(self.driver).click('id', 'tab-fbt')
            time.sleep(2)
            # 点击产业下拉框
            js = 'document.querySelector("#pane-fbt > div > div.control > div > div > span > span > i").click()'
            self.driver.execute_script(js)
            time.sleep(3)
            # 切换新材料
            js2 = 'document.getElementsByClassName("el-select-dropdown__item")[1].click()'
            self.driver.execute_script(js2)
            time.sleep(2)
            # 获取新材料的class值
            js3 = 'return document.getElementsByClassName("el-select-dropdown__item")[1].getAttribute("class")'
            classvalue = self.driver.execute_script(js3)
            self.assertIn('selected', classvalue, '用例执行失败')
        except Exception:
            self.add_img()
            raise


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
