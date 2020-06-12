
from common.common_rwcd import Common_Read
from common.Script import Script_Case
import os
from selenium import webdriver
from page.czx_login_page import LoginPage




class Currency_Script():
    '''课程页面操作类'''
    def __init__(self,driver,execl_name,sheet_name,data_Catalog="data",copy_execl_name="wait_time.xls"):

        #获取浏览器操作句柄
        self.driver = driver

        #获取数据excel表文件位置，及从具体工作薄获取浏览器操作步骤数据
        config_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        filepath = os.path.join(os.path.join(config_path,data_Catalog),execl_name)
        filepath2 = os.path.join(os.path.join(config_path,data_Catalog),copy_execl_name)

        #读取excel文件，并实例化
        data = Common_Read(filepath,sheetName=sheet_name) #cze_Learn_course为工作溥名称
        data2 = Common_Read(filepath2,'wait_time')

        #转化excel文件数据为可操作字典数据
        self.data_value = data.dict_data()
        self.time_data =  data2.dict_data()


    def currency_scirpt_case(self,username,path="",screenshot_path=""):

        #实例化浏览器操作类
        script = Script_Case(self.driver,username,self.time_data,path,screenshot_path)

        #调用浏览器操作执行函数
        self.driver = script.script_case(self.data_value)
        return self.driver

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://192.168.50.65")
    driver.maximize_window()
    test_login = LoginPage(driver)
    driver = test_login.login("test_student","qaz123456")
    currency = Currency_Script(driver,execl_name="czx_data.xls",sheet_name="czx_open_vm")
