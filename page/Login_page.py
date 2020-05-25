from common.base import Base
from selenium import webdriver
from common.common_rwcd import Common_Read
import time,os


class LoginPage():
    '''登录类'''
    def __init__(self,driver):
        #获取浏览器句柄
        self.driver = driver

        #将被操作的excel文件路径，及具体工作薄
        real_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(os.path.join(real_path,"data"),"cze_data.xls")
        sheetName = "login" #工作薄内容为登录的操作步骤数据

        #读取excel文件，并实例化
        data = Common_Read(data_path, sheetName)

        #转化excel文件数据为可操作字典数据
        self.data_value = data.dict_data()

        #实例化浏览器基本操作类
        self.b = Base(self.driver)

    def login(self,username,password):
        '''用户登录函数'''
        list_value = {}
        for i in range(len(self.data_value)):
            list_value["loca%d" %(i+1)] = (self.data_value[i]["type"],self.data_value[i]["value"])

        #调用浏览器中基本操作事件函数，如：send(定位元素并填入数据)、click(定位元素，并点击）
        self.b.send(list_value["loca1"],username)
        self.b.send(list_value["loca2"],password)
        time.sleep(1)
        self.b.click(list_value["loca3"])
        # self.driver.get_screenshot_as_file(r"C:\Users\safecode\Desktop\selenium_bug\%s_login_Result.png" %username)
        time.sleep(1)
        return self.driver

    def login_test(self,username,password):
        '''用户登录函数'''
        print(username,password)
        list_value = {}
        for i in range(len(self.data_value)):
            list_value["loca%d" %(i+1)] = (self.data_value[i]["type"],self.data_value[i]["value"])

        #调用浏览器中基本操作事件函数，如：send(定位元素并填入数据)、click(定位元素，并点击）
        self.b.send(list_value["loca1"],username)
        time.sleep(1.5)
        self.b.send(list_value["loca2"],password)
        time.sleep(1.5)
        self.b.click(list_value["loca3"])
        time.sleep(5)
        # time.sleep(1)
        # loca = ("xpath",".//*[@id='contentMain']/ul/li[7]/span")
        # flag = self.b.text_in_element(loca,"设置")
        # if flag != False:
        #     print("用户：%s，登录成功！" %username)
        # else:
        #     print("用户：%s，登录失败！" %username)
        # time.sleep(5)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://192.168.235.143/#/login")
    c = LoginPage(driver)
    c.login("test_j","qaz123456")