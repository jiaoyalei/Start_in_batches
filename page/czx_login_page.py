from common.base import Base
from tomorrow import threads
from selenium import webdriver
from common.common_rwcd import Common_Read
import time
import os
from Verification_Code.yzm_get_text import Yzm_get

class LoginPage():
    '''登录类'''
    def __init__(self,driver):
        #获取浏览器句柄
        self.driver = driver

        #将被操作的excel文件路径，及具体工作薄
        real_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(os.path.join(real_path,"data"),"czx_data.xls")
        sheetName = "czx_login" #工作薄内容为登录的操作步骤数据

        #读取excel文件，并实例化
        data = Common_Read(data_path, sheetName)

        #转化excel文件数据为可操作字典数据
        self.data_value = data.dict_data()

        #实例化浏览器基本操作类
        self.b = Base(self.driver)

    def login(self,username,password):
        '''用户登录函数'''
        list_value = {}
        # image_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # image_url = os.path.join(image_path,'image')
        for i in range(len(self.data_value)):
            list_value["loca%d" %(i+1)] = (self.data_value[i]["type"],self.data_value[i]["value"])
        time.sleep(1)
        #调用浏览器中基本操作事件函数，如：send(定位元素并填入数据)、click(定位元素，并点击）
        self.b.send(list_value["loca1"],username)
        self.b.send(list_value["loca2"],password)
        # flag = True
        # while flag == True:
        #     text = self.b.find(list_value["loca3"]).text()
        #     print(text)
        #     if len(text) == 4:
        #         flag=False
        #     time.sleep(3)
        # self.b.send(list_value["loca3"],"1111")
        # yzm_text = Yzm_get(self.driver).yzm_text_get(image_url)
        # self.b.send(list_value["loca3"],yzm_text)
        # self.b.click(list_value["loca4"])
        # time.sleep(5)
        falg = True
        while falg:
            try:
                loca = ("xpath",".//*[@id='main']/div/div[1]/div/div[3]/div/div[1]/a")
                self.b.find(loca)
                falg = False
            except Exception as e:
                time.sleep(0.5)
                flag = self.b.find(list_value["loca5"])
                flag.clear()
                image_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
                image_url = os.path.join(image_path,'image')
                yzm_text = Yzm_get(self.driver).yzm_text_get(image_url)
                self.b.send(list_value["loca3"],yzm_text)
                self.b.click(list_value["loca4"])
                time.sleep(0.5)
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
    driver.get("https://192.168.50.65/#/login")
    c = LoginPage(driver)
    c.login("test_student","qaz123456")