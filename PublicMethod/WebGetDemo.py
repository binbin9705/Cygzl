from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class Runmian():
    def __init__(self, driver):
        self.driver = driver

    # 浏览器参数设置
    def options(self):
        option = Options()  # Options类实例化
        # option.add_argument('--incognito')# 无痕模式
        option.add_argument('no-sandbox')  # 以最高权限运行
        option.add_argument('--start-maximized')  # 最大化运行（全屏窗口）设置元素定位比较准确
        option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        # 关闭“chrome正受到自动测试软件的控制”
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option("detach", True)  # 不自动关闭浏览器
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
        elif type == "css":
            el = self.driver.find_element(By.CSS_SELECTOR, value)
        return el

    # 对定位到元素进行点击
    def click(self, type, value):
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        # 调用click()进行点击操作
        el.click()

    # 获取元素text文本
    def obtaintest(self, type, value):
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        # 返回
        return el.text

    # 获取任意元素值
    def obtainvalue(self, valuename, type, value):
        '''class,title,name'''
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        # 返回
        return el.get_attribute(valuename)

    # 输入
    def input_data(self, type, value, data):
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        # 调用send_keys进行输入
        el.send_keys(data)

    # 切换title页
    def switch_window_by_title(self, title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title.__contains__(title):
                break

    # 切换frame
    def switch_window_by_frame(self, frame):
        self.driver.switch_to.frame(frame)
