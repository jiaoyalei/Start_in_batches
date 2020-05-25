import time
from page.czx_login_page import LoginPage
from tomorrow import threads
import os
from page.currency_page import Currency_Script
from common.select_webdriver import Select_Webdriver
from common.common_rwcd import Common_Read



class demo():

    '''日志、录屏并发'''
    def __init__(self):
        real_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(os.path.join(real_path,"data"),"czx_data.xls") #获取数据文件路径

        self.url = Common_Read().get_config_data("czx_url") #由配置文件读取测试地址
        self.data_value = Common_Read(data_path, 'user').dict_data() #由数据文件读取用户信息并转换为字典数据
        Common_Read().add_waittime_excel()

    @threads(40)
    def login(self,i):
        #加载登录时的账号密码数据
        user_data = self.data_value[i]  # i  用户信息下标
        username,password = user_data["username"],user_data["password"]


        #打开浏览器至指定页面
        driver = Select_Webdriver("Chrome").webdriver_open()
        driver.get(self.url)

        #登录操作
        Login = LoginPage(driver)
        driver = Login.login(username,password)

        #创建任务
        Course = Currency_Script(driver,execl_name="czx_data.xls",sheet_name="czx_log_Concurrent")
        driver = Course.currency_scirpt_case(username)
        return driver





if __name__ == "__main__":
    d = demo()
    for i in range(10):
        d.login(i)
        time.sleep(5)

