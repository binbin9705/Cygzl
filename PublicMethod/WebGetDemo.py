import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
class Runmian():
    def __init__(self,driver):
        self.driver = driver
    #浏览器参数设置
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
    #登录
    def login(self, username, password):
        '''输入用户名和密码,点击登录'''
        Runmian(self.driver).input_data("name","username",username)
        # self.driver.find_element(By.NAME, 'username').send_keys(username)
        time.sleep(1)
        # self.driver.find_element(By.NAME, 'password').send_keys(password)
        Runmian(self.driver).input_data('name', 'password', password)
        time.sleep(1)
        # self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/button').click()
        Runmian(self.driver).click('xpath','//*[@id="app"]/div/form/button')
        time.sleep(1)
    # 打开网页功能
    def open(self,url):
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
            el = self.driver.find_element(By.ID,value)
        elif type == "name":
            el = self.driver.find_element(By.NAME,value)
        elif type == "class_name":
            el = self.driver.find_element(By.CLASS_NAME,value)
        elif type == "tag_name":
            el = self.driver.find_element(By.TAG_NAME,value)
        elif type == "link_text":
            el = self.driver.find_element(By.LINK_TEXT,value)
        elif type == "partial_link_text":
            el = self.driver.find_element(By.PARTIAL_LINK_TEXT,value)
        elif type == "xpath":
            el = self.driver.find_element(By.XPATH,value)
        elif type == "css_selector":
            el = self.driver.find_element(By.CSS_SELECTOR,value)
        return el

    #对定位到元素进行点击
    def click(self,type,value):
        # 调用locateElement定位元素
        el=self.locateElement(type,value)
        #调用click()进行点击操作
        el.click()

    # 对定位到元素进行输入
    def input_data(self, type, value,data):
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

    #截图
    def jietu(self,url):
        self.driver.get_screenshot_as_file(url)







