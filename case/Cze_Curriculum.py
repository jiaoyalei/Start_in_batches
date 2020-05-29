import time,os
from page.Login_page import LoginPage
from tomorrow import threads
from page.currency_page import Currency_Script
from common.select_webdriver import Select_Webdriver
from common.common_rwcd import Common_Read as CR




class Batch_Open_Curriculum_Vm():
    '''批量开启虚机类——课程'''
    def __init__(self):
        '''加载测试地址、页面操作数据、清理上次运行产生的截图'''
        self.url = CR().get_config_data('cze_url') #由配置文件读取测试地址

        #获取数据文件路径并将对应sheet页面操作数据转换为字典格式
        real_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(os.path.join(real_path,"data"),"cze_data.xls") #获取数据文件路径
        self.data_value = CR(data_path, 'user_elective').dict_data() #由数据文件读取用户信息并转换为字典数据

        CR().add_waittime_excel()  #复制生成data.xls文件，存放定时时间数据

        #清除上次程序运行产生的所有截图
        CR().clear_screenshot(r"C:\Users\safecode\Desktop\cze_curriculum_open_vm")
        CR().clear_screenshot(r"C:\Users\safecode\Desktop\curriculum_open")
    @threads(80)
    def curriculum_vm_script(self,i):
        #加载登录时的账号密码数据
        user_data = self.data_value[i]  # i  用户信息下标
        username,password = user_data["username"],user_data["password"]

        #打开浏览器并访问指定url地址
        driver = Select_Webdriver("Chrome").webdriver_open()
        driver.get(self.url)

        #登录操作
        Login = LoginPage(driver)
        driver = Login.login(username,password)

        #学习课件打开虚机操作
        Course = Currency_Script(driver,execl_name="cze_data.xls",sheet_name="cze_Learm_Curriculum")
        driver = Course.currency_scirpt_case(username)



if __name__ == "__main__":
    script = Batch_Open_Curriculum_Vm()
    for i in range(30):
        script.curriculum_vm_script(i)
        time.sleep(3)

