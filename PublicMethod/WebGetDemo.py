import os
import traceback

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
import sys


class Runmian():
    def __init__(self, driver):
        self.driver = driver

    # 浏览器参数设置
    def options(self):
        # Options类实例化
        option = Options()
        # 关闭“chrome正受到自动测试软件的控制”
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 不自动关闭浏览器
        option.add_experimental_option("detach", True)
        # 关掉浏览器记住密码弹窗
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        option.add_experimental_option("prefs", prefs)
        return option

    # 登录
    def login(self, username, password):
        '''输入用户名和密码,点击登录'''
        Runmian(self.driver).input_data("name", "username", username)
        # self.driver.find_element(By.NAME, 'username').send_keys(username)
        time.sleep(1)
        # self.driver.find_element(By.NAME, 'password').send_keys(password)
        Runmian(self.driver).input_data('name', 'password', password)
        time.sleep(1)
        # self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/button').click()
        Runmian(self.driver).click('xpath', '//*[@id="app"]/div/form/button')
        time.sleep(1)

    # 打开网页功能
    def open(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    # 关闭当前窗口
    def close(self):
        # time.sleep(3)
        self.driver.close()

    # 退出驱动并关闭所有关联的窗口。
    def quit(self):
        # time.sleep(3)
        self.driver.quit()

    # 定位元素
    def locateElement(self, type, value):
        if type == "id":
            el = self.driver.find_element(By.ID, value)
        elif type == "name":
            el = self.driver.find_element(By.NAME, value)
        elif type == "class_name":
            el = self.driver.find_element(By.CLASS_NAME, value)
        elif type == "tag_name":
            el = self.driver.find_element(By.TAG_NAME, value)
        elif type == "link_text":
            el = self.driver.find_element(By.LINK_TEXT, value)
        elif type == "partial_link_text":
            el = self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
        elif type == "xpath":
            el = self.driver.find_element(By.XPATH, value)
        elif type == "css_selector":
            el = self.driver.find_element(By.CSS_SELECTOR, value)
        return el

    # 对定位到元素进行点击
    def click(self, type, value):
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        # 调用click()进行点击操作
        el.click()

    #获取元素text文本
    def obtaintest(self,type,value):
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        #获取文本
        return el.text


    # 对定位到元素进行输入
    def input_data(self, type, value, data):
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        # 调用send_keys进行输入
        el.send_keys(data)

    # 获取定位到的元素中的文本内容<a>text</a>
    def getText(self, type, value):
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        # 返回文本内容
        return el.text

    # 截图
    def jietu(self, url):
        self.driver.get_screenshot_as_file(url)
        # WebGetDemo.Runmian(self.driver).jietu("D:\pycharm\Cygzl\error_png\\test_01\error02.png")

    # 构造今天的日期字符串
    def currentDate(self):
        date = time.localtime()
        today = str(date.tm_year) + "-" + str(date.tm_mon) + "-" + str(date.tm_mday)
        return today

    # 构造当前时间字符串
    def currentTime(self):
        timeStr = datetime.now()
        now = timeStr.strftime('%H - %M - %S')
        return now

    # 创建图片存储路径
    def createDir(self):
        # 获取当前文件所在目录的绝对路径
        # currentPath = os.path.dirname(os.path.abspath(__file__))
        # 获取今天的日期字符串
        today = Runmian(self).currentDate()
        # print(today,"1")
        # 构造以今天日期命名的目录的绝对路径
        dateDir = os.path.join('D:\pycharm\Cygzl\error_png', today)
        # print(dateDir,"2")
        if not os.path.exists(dateDir):
            # 如果以今天日期命名的目录不存在则创建
            os.mkdir(dateDir)
        now = Runmian(self).currentTime()
        # 构造以当前时间命名的目录的绝对路径
        timeDir = os.path.join(dateDir, now)
        print(timeDir, "3")
        # if not os.path.exists(timeDir):
        #     os.mkdir(timeDir)
        return timeDir

    # 封装截屏方法
    def takeScreenshot(self, savePath, picName):
        # 构造屏幕截图路径及图片名
        picPath = os.path.join(savePath + '.png')
        try:
            # 调用WebDriver提供的get_screenshot_as_file()方法
            # 将截取的屏幕图片保存为本地文件
            self.driver.get_screenshot_as_file(picPath)
        except Exception as e:
            print(traceback.print_exc())
