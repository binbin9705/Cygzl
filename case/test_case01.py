import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from PublicMethod import WebGetDemo
import warnings


class Test01(unittest.TestCase):
    '''页面跳转'''

    @classmethod
    def setUpClass(cls):
        # 启动浏览并设置相关选项
        cls.driver = webdriver.Chrome(options=WebGetDemo.Runmian(cls).options())
        WebGetDemo.Runmian(cls.driver).open('http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard')
        WebGetDemo.Runmian(cls.driver).login(username='ihqd-test', password='ihqd-test@6688')
        cls.driver.refresh()
        # 消除警告
        warnings.simplefilter('ignore', ResourceWarning)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        # 启动浏览并设置相关选项
        self.imgs = []
    def add_img(self):
        # 1、下面注释掉的这行代码作用是不管用例是否执行成功，只要在执行过程加了self.add_img()操作，那么最后生成的报告中含有该执行过程的截图，如果不添加则默认对用例失败进行截图
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def tearDown(self):
        self.driver.refresh()
        # pass
    # @unittest.skip("跳过")
    def test_01(self):
        '''首页跳转CRL指数页面'''
        try:
            # 登录后判断网页标题是否是"首页 - 产业高质量发展平台"是的话执行后续的代码，反之等待10s后报错误信息
            WebGetDemo.Runmian(self.driver).selp('titleis', titlevalue='首页 - 产业高质量发展平台')
            # 等待页面全部加载完成后执行后续代码
            WebGetDemo.Runmian(self.driver).selp('elementkj', 'css', 'div[class =g2-tooltip]')
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 0)
            # 点击CRI指数
            WebGetDemo.Runmian(self.driver).click('link_text', 'CRI指数')
            # 页面跳转后 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", 'id', 'container4')
            # 判断页面title是否等于预期title
            self.assertEqual('CRI指数 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_02(self):
        '''首页跳转企业总量页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", 'id', 'container4')
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 0)
            # 点击企业总量
            WebGetDemo.Runmian(self.driver).click('link_text', '企业总量')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj","id","container3")
            # 判断跳转后的标签页是不是企业总量
            self.assertEqual('企业总量 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_03(self):
        '''首页跳转行业分析页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "container3")
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 0)
            # 点击行业分析
            WebGetDemo.Runmian(self.driver).click('link_text', '行业分析')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "container8")
            self.assertEqual('行业分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_04(self):
        '''首页跳转结构分析页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "container8")
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 0)
            # 点击结构分析
            WebGetDemo.Runmian(self.driver).click('link_text', '结构分析')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "container6")
            self.assertEqual('结构分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_05(self):
        '''首页跳转重点企业页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "container6")
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 0)
            # 点击重点企业
            WebGetDemo.Runmian(self.driver).click('link_text', '重点企业')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "container6")
            self.assertEqual('重点企业 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_06(self):
        '''首页跳转总体监测页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "container6")
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 1)
            # 点击整体概览
            WebGetDemo.Runmian(self.driver).click('link_text', '整体概览')
            self.assertEqual('总体监测 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_07(self):
        '''首页跳转产业分析页面'''
        try:
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 1)
            # 点击产业分析
            WebGetDemo.Runmian(self.driver).click('link_text', '产业分析')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "cyfxView")
            self.assertEqual('产业分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_08(self):
        '''首页跳转产业地图页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "cyfxView")
            # 点击产业地图
            WebGetDemo.Runmian(self.driver).click('link_text', '产业地图')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "hyChart")
            self.assertEqual('产业地图 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_09(self):
        '''首页跳转创新主体页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "hyChart")
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 2)
            # 点击创新主体
            WebGetDemo.Runmian(self.driver).click('link_text', '创新主体')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "class_name", "amap-layers")
            self.assertEqual('创新主体 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_10(self):
        '''首页跳转创新成果页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "class_name", "amap-labels")
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 2)
            # 点击创新成果
            WebGetDemo.Runmian(self.driver).click('link_text', '创新成果')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "class_name", "amap-layer")
            self.assertEqual('创新成果 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_11(self):
        '''首页跳转产业链图谱页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "class_name", "amap-layer")
            # 点击产业链图谱
            WebGetDemo.Runmian(self.driver).click('link_text', '产业链图谱')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "imgLoad")
            self.assertEqual('产业链图谱 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_12(self):
        '''首页跳转招商图谱页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "imgLoad")
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 3)
            # 点击招商图谱
            WebGetDemo.Runmian(self.driver).click('link_text', '招商图谱')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "imgLoad")
            self.assertEqual('招商图谱 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_13(self):
        '''首页跳转资本流动页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "imgLoad")
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 3)
            # 点击资本流动
            WebGetDemo.Runmian(self.driver).click('link_text', '资本流动')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "class_name", "inv_h3")
            self.assertEqual('资本流动 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_14(self):
        '''首页跳转开发发展-结构分析页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "class_name", "inv_h3")
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 4)
            # 点击结构分析
            WebGetDemo.Runmian(self.driver).click('link_text', '结构分析')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "container6")
            self.assertEqual('结构分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_15(self):
        '''首页跳转地域分析页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "container6")
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 4)
            # 点击地域分析
            WebGetDemo.Runmian(self.driver).click('link_text', '地域分析')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "container7")
            self.assertEqual('地域分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_16(self):
        '''首页跳转企业分析页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "container7")
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 4)
            # 点击企业分析
            WebGetDemo.Runmian(self.driver).click('link_text', '企业分析')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "class_name", "screenM")
            self.assertEqual('企业分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_17(self):
        '''首页跳转总体概览页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "class_name", "screenM")
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 5)
            # 点击总体概览
            WebGetDemo.Runmian(self.driver).click('link_text', '总体概览')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "containerztglSH")
            self.assertEqual('总体概览 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise

    # @unittest.skip("跳过")
    def test_18(self):
        '''首页跳转结构分析页面'''
        try:
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "containerztglSH")
            # 点击导航下拉选择框
            WebGetDemo.Runmian(self.driver).click('class_names', 'el-submenu__icon-arrow', 5)
            # 点击总体概览
            WebGetDemo.Runmian(self.driver).click('link_text', '结构分析')
            # 判断页面是否加载完成
            WebGetDemo.Runmian(self.driver).selp("elementkj", "id", "container6")
            self.assertEqual('结构分析 - 产业高质量发展平台', self.driver.title, '用例执行错误')
            time.sleep(1)
        except Exception:
            self.add_img()
            raise


if __name__ == '__main__':
    login_url = 'http://ihd.wanvdata.cn/#/login?redirect=%2Fdashboard'
    name = 'ihqd-test'
    password = 'ihqd-test@6688'
    unittest.main(verbosity=2)
