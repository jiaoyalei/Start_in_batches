import time
from common.read_excel import ExcelUtil
from page.czx_login_page import LoginPage
from tomorrow import threads
import os
from common.read_config import Read_Conf as r_c
from page.czx_task_page_demo import Task_Details
from common.select_webdriver import Select_Webdriver
import unittest,ddt



real_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(os.path.join(real_path,"data"),"czx_user.xls") #获取数据文件路径
data_value = ExcelUtil(data_path, 'user2').dict_data() #由数据文件读取用户信息并转换为字典数据

@ddt.ddt
class Test_vm_status(unittest.TestCase):

    '''批量登录查看vM开机状态'''

    @threads(30)
    @ddt.data(*data_value)
    def test_login(self,data_value):
        #加载登录时的账号密码数据


        #打开浏览器至指定页面

        driver = Select_Webdriver("Chrome","no-head").webdriver_open()
        driver.get("https://192.168.50.66")

        #登录操作
        Login = LoginPage(driver)
        driver = Login.login(data_value["username"],data_value["password"])

        #创建任务
        Course = Task_Details(driver)
        driver = Course.course_ware(data_value["username"])
        return driver





if __name__ == "__main__":
    unittest.main()


