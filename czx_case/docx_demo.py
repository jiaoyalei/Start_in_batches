import time,os
from page.czx_login_page import LoginPage
from tomorrow import threads
from common.select_webdriver import Select_Webdriver
from common.common_rwcd import Common_Read
from page.currency_page import Currency_Script
from docx import Document


class demo():

    '''批量开启虚机类——选修'''
    def __init__(self):
        real_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(os.path.join(real_path,"data"),"czx_data.xls") #获取数据文件路径

        self.url = Common_Read().get_config_data("czx_url") #由配置文件读取测试地址
        self.data_value = Common_Read(data_path, 'user').dict_data() #由数据文件读取用户信息并转换为字典数据
        Common_Read().add_waittime_excel()
        time_value = int(time.time())
        kc_path = r"C:\Users\safecode\Desktop\jietu\kecheng"
        self.kc_jt_path = os.path.join(kc_path,"kecheng%d\\"%time_value)
        if not os.path.exists(self.kc_jt_path): os.mkdir(self.kc_jt_path)


        self.path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"test_report"),"性能测试报告%d.docx" %time_value)
        print(self.path)
        self.doc = Document()
        self.doc.add_heading('性能测试结果',0)
        self.doc.save(self.path)

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

        #修改指定任务并批量创建VM
        Course = Currency_Script(driver,execl_name="czx_data.xls",sheet_name="docx_demo")
        driver = Course.currency_scirpt_case(username,self.path,self.kc_jt_path)
        return driver




if __name__ == "__main__":
    d = demo()
    for i in range(5):
        d.login(i)
        time.sleep(2)

