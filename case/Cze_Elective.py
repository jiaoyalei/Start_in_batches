from selenium import webdriver
import time
from page.Login_page import LoginPage
from tomorrow import threads
import os
from page.currency_page import Currency_Script
from common.select_webdriver import Select_Webdriver
from common.common_rwcd import Common_Read
from docx import Document

class demo():

    '''批量开启虚机类——选修'''
    def __init__(self):
        real_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(os.path.join(real_path,"data"),"cze_data.xls") #获取数据文件路径

        self.url = Common_Read().get_config_data("cze_url") #由配置文件读取测试地址
        self.data_value = Common_Read(data_path, 'user_elective').dict_data() #由数据文件读取用户信息并转换为字典数据
        Common_Read().add_waittime_excel()
        Common_Read().clear_screenshot(r"C:\Users\safecode\Desktop\cze_elective_open_vm")
        Common_Read().clear_screenshot(r"C:\Users\safecode\Desktop\elective_open")
        time_value = int(time.time())
        self.path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"test_report"),"课程性能测试报告%d.docx" %time_value)
        print(self.path)
        self.doc = Document()
        self.doc.add_heading('性能测试开机结果',0)
        self.doc.save(self.path)

    @threads(30)
    def login(self,i):
        #加载登录时的账号密码数据

        # self.data_value[i] = {"username":"testb47","password":"Safecode@123"}
        data_value_demo = self.data_value[i]  # i  账号密码获取顺序号，例：第一次取test1,第二次取test2，对应账号密码列表中下标

        #打开浏览器至指定页面
        driver = Select_Webdriver("Chrome").webdriver_open()
        driver.get(self.url)

        #登录操作
        Login = LoginPage(driver)
        driver = Login.login(data_value_demo["username"],data_value_demo["password"])

        #学习课件打开虚机操作
        Course = Currency_Script(driver,execl_name="cze_data.xls",sheet_name="cze_Learm_Elective")
        driver = Course.currency_scirpt_case(data_value_demo["username"],self.path)
        return driver





if __name__ == "__main__":
    d = demo()
    for i in range(2):
        d.login(i)
        time.sleep(5)

