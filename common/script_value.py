from common.base import Base
import time,datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os,traceback
from common.logger import Log
from selenium import webdriver
import pyautogui as pag
from common.common_rwcd import Common_Read


start_value = Common_Read().get_config_data("value")
x = False
find_result = True
vm_name = {}
start_time = ""
over_time = ""
open_vm_time_all = {}
open_vm_start_time = {}
open_vm_end_time = {}


class Script_value(Base):
    '''使用selenium界面操作封装方法'''

    def __init__(self,driver,time_data=""):
        self.driver = driver
        global start_time
        global over_time
        global open_vm_time
        open_vm_time = {}
        if time_data != "":
            start_time = time_data[0]['start_time']
            over_time = time_data[0]['over_time']
        self.log = Log()

    def click_script(self,locator,value="",username=""):
        '''页面元素单击操作'''
        global open_vm_start_time
        if value["notes"] == "点击开机按钮":
            start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            open_vm_start_time.update(eval("{'%s':'%s'}"%(username,start_time)))
        self.click(locator)
        if value["notes"] == "点击开机按钮":
            self.driver.get_screenshot_as_file(r"%s%s_open.png" %(value["screenshot_url"],username))
        return self.driver

    def click_random_script(self,locator,value="",username=""):
        self.click(locator)
        return self.driver

    def to_iframe(self,locator,value="",username=""):
        '''切换至指定的iframe'''
        self.switch_to(value['value'])
        return self.driver

    def is_element_exis_script(self,locator,value="",username=""):
        '''判断页面元素是否存在'''
        flag = self.is_element_exist(locator,value['time_out'])
        if flag == True:
            print("%s开机成功！",username)
        return self.driver

    def is_element_exist_and_click_script(self,locator,value="",username=""):
        '''判断页面元素是否存在，若存在则点击该元素'''
        if value['time_out'] == "" : value['time_out']=5
        flag = self.is_element_exist(locator,int(value['time_out']))
        time.sleep(2)
        if flag == True:
            self.click(locator)
        return self.driver

    def is_element_exist_click_script(self,locator,value="",username=""):
        '''判断页面特定文本元素是否存在，若存在则点击其它元素'''
        if value['time_out'] == "" : value['time_out']=5
        self.text_result = self.find(locator,time_out=int(value["time_out"]))
        self.text_value = self.text_result.text
        locator2 = (value["types"],value["values"])
        time.sleep(2)
        while True:
            if self.text_value == value["check"]:
                self.click(locator2)
                break
            else:
                try:
                    self.text_result = self.find(locator,time_out=int(value["time_out"]))
                    self.text_value = self.text_result.text
                except Exception:
                    error = traceback.format_exc()
                    self.log.error("%s:【%s】" %(username,value["notes"])+error)
        return self.driver

    def is_element_exist_click_plus_script(self,locator,value="",username=""):
        '''判断页面特定文本元素是否存在，若存在则点击其它元素'''
        for i in range(1,11):
            search_for_elements = value["values"]
            wait_click_elements = value["value"]

            search_locator= (value["type"],search_for_elements.replace("flag","%d" %i))
            wait_click_locator = (value["types"],wait_click_elements.replace("flag","%d" %i))
            # self.log.info("search_locator:%s" %search_for_elements.replace("flag","%d" %i))
            # self.log.info("wait_click_locator:%s" %wait_click_elements.replace("flag","%d" %i))
            try:
                self.text_result = self.find(search_locator)
                self.text_value = self.text_result.text
                # print("元素文本信息:%s,type:%s" %(self.text_value,type(self.text_value)))
                # print("检查点:%s,type:%s" %(value["check"],type(value["check"])))
                if self.text_value == value["check"]:
                    self.click(wait_click_locator)
                    break
            except Exception as e:
                error = traceback.format_exc()
                self.log.error("%s:【%s】" %(username,value["notes"])+error)
                continue

    def send_script(self,locator,value="",username=""):
        '''页面填写数据操作'''
        self.send(locator,value['send_value'])
        return self.driver

    def send_random_script(self,locator,value="",username=""):
        '''名称后增加随机数，用于系统不可重名限制'''
        global start_value
        self.send(locator,(value['send_value']+"00"+str(start_value)))
        start_value = start_value + 1
        return self.driver

    def time_script(self,locator,value="",username=""):
        '''用于各操作之间的时间等待'''
        if value["send_value"] == "":value["send_value"]=2
        time.sleep(int(value["send_value"]))
        return self.driver

    def move_script(self,locator,value="",username=""):
        '''页面元素单击操作'''
        self.move(locator)
        return self.driver

    def switch_content_script(self,locator="",value="",username=""):
        '''由某iframe返回至页面顶层'''
        self.driver.switch_to.default_content()
        return self.driver

    def execution_script_forto(self,locator,value="",username=""):
        '''滑动至页面底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def script_js_forto(self,locator,value="",username=""):
        '''指定移动至何位置'''
        print(value['value'],value['send_value'])
        js = 'document.getElementsByClassName("%s").scrollTop=%s' %(value['value'],value['send_value'])
        self.driver.execute_script(js)
        return self.driver

    def window_handles_script(self,locator,value="",username=""):
        '''切换至跳转的新页面'''
        while True:
            try:
                n = self.driver.window_handles # 获取当前页句柄
                self.driver.switch_to.window (n[-1]) # 切换到新的网页窗口
                break
            except Exception as e:
                # error = traceback.format_exc()
                # self.log.error(error)
                pass
        return self.driver

    def to_iframe_xpath_script(self,locator,value="",username=""):
        '''通过iframe的xpath定位iframe'''
        element = self.find(locator)
        self.switch_to(element)
        return self.driver

    def move_perform_click_script(self,locator,value="",username=""):
        '''将鼠标移动至页面的指定位置单击'''
        x,y = int(value['types']),int(value['values'])
        print(x,y)
        ActionChains(self.driver).move_by_offset(x,y).click().perform()
        return self.driver

    def move_perform_script(self,locator,value="",username=""):
        '''将鼠标移动至页面的指定位置右键'''
        x,y = int(value['types']),int(value['values'])
        now_x,now_y = pag.position()
        print("now_x:%s,now_y:%s" %(str(now_x),str(now_y)))
        ActionChains(self.driver).move_by_offset(-int(now_x), -int(now_y)).perform()
        now_x2,now_y2 = pag.position()
        print("now_x:%s,now_y:%s" %(-int(now_x),-int(now_y)))
        ActionChains(self.driver).move_by_offset(x,y).context_click().perform()

        return self.driver

    def get_text_script(self,locator,value="",username=""):
        '''获取指定元素的文本信息'''
        global vm_name
        if value["time_out"] == "":value["time_out"]=5
        try:
            self.text_result = self.find(locator,time_out=int(value["time_out"]))
            self.text_value = self.text_result.text
            vm_name.update(eval("{'%s':'%s'}" %(username,self.text_value)))
        except Exception as e:
            vm_name.update(eval("{'%s':'开机超时或虚机未开启！'}" %(username)))
        if len(vm_name) == 20:
            for i in vm_name:
                print(i,":",vm_name[i])
        return self.driver

    def get_text_and_status_script(self,locator,value="",username=""):
        '''每秒进行一次页面内容查找，并判断内容结果'''
        global open_vm_end_time
        global open_vm_start_time
        find_text_time = int(value["time_out"])
        start_value = 0
        error = ""
        flag = True
        while start_value < find_text_time:
            start_value = start_value + 1
            try:
                text_result = self.find(locator)
                text_value = text_result.text
                if value["check"] in text_value:
                    flag = False
                    end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    open_vm_end_time.update(eval("{'%s':'%s'}"%(username,end_time)))
                    start_time = datetime.datetime.strptime(open_vm_start_time[username],'%Y-%m-%d %H:%M:%S')
                    end_time = datetime.datetime.strptime(open_vm_end_time[username],'%Y-%m-%d %H:%M:%S')
                    time_value = end_time - start_time
                    self.driver.get_screenshot_as_file(r"%s%s_%ss_success.png" %(value["screenshot_url"],username,time_value.seconds))
                    print("用户：%s-->%s-->:开机用时%s秒" %(username,text_value,time_value.seconds))
                    print("%s-start:%s,-end:%s"%(username,open_vm_start_time[username],open_vm_end_time[username]))
                    break

            except Exception as e:
                error = traceback.format_exc()
                print(error)
                try:
                    self.switch_content_script()
                    loca = ("xpath","html/body/div/div/div[2]/div[2]/iframe")
                    element = self.find(loca)
                    self.switch_to(element)

                except Exception as e:
                    pass
            time.sleep(1)
        if flag == True:
            end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            open_vm_end_time.update(eval("{'%s':'%s'}"%(username,end_time)))
            end_time = datetime.datetime.strptime(open_vm_end_time[username],'%Y-%m-%d %H:%M:%S')
            start_time = datetime.datetime.strptime(open_vm_start_time[username],'%Y-%m-%d %H:%M:%S')
            time_value = end_time - start_time
            self.driver.get_screenshot_as_file(r"%s%s_%ss_fail.png" %(value["screenshot_url"],username,time_value.seconds))
            print("用户%s:开机异常！错误截图位置：%s%s_%ss_fail.png" %(username,value["screenshot_url"],username,time_value.seconds))
        if error !="":
            self.log.error("%s:【%s】" %(username,value["notes"])+error)

    def get_vm_state_script(self,locator,value="",username=""):
        '''获取虚机开启状态内容文本'''
        global vm_name
        if value["check"] in vm_name[username]:
            print("用户：%s-->%s-->:已于5秒内开机！" %(username,vm_name[username]))

        else:
            print("用户：%s-->5秒内开机结果为:%s" %(username,vm_name[username]))
        return self.driver

    def get_czx_vm_state_script(self,locator,value="",username=""):
        '''获取虚机开启状态内容文本'''
        global vm_name
        if value["check"] in vm_name[username]:
            print("用户：%s-->%s-->已开机！" %(username,vm_name[username]))

        else:
            print("用户：%s-->%s-->未开机！" %(username,vm_name[username]))
        return self.driver

    def text_in_element_script(self,locator,value="",username=""):
        '''判断页面文本元素是否存在'''
        global x
        self.falg = self.text_in_element(locator,value["check"])
        if self.falg != False:
            x = True
        else:
            x = False
            print("执行全局变量赋值，此时X是：",x)
        return self.driver

    def baidu_demo_script(self,locator,value="",username=""):
        global x
        if x == True:
            self.refresh_script()
        return self.driver

    def refresh_script(self,locator="",value="",username=""):
        '''对页面进行刷新操作'''
        self.driver.refresh()
        return self.driver

    def drag_element_script(self,locator,value="",username=""):
        '''向右拖动元素   '''
        action_chains = ActionChains(self.driver)
        dragElement = self.find(locator)
        #将元素向右拖动指定距离
        action_chains.drag_and_drop_by_offset(dragElement,int(value['send_value']),0).perform()
        return self.driver

    def drag_and_drop(self,locator,value="",username=""):
        '''拖拽元组至拓扑图'''
        start = self.find(locator)
        loca2 = (value['types'],value['send_value'])
        end = self.find(loca2)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(start, end)
        # 执行
        actions.perform()
        return self.driver

    def select_script(self,locator,value="",username=""):
        '''从select下拉框中选中数据'''
        self.select(locator,value["types"],value['values'])
        return self.driver

    def screenshot_script(self,locator,value="",username=""):
        global vm_name
        # print('screenshot是{},value["check"]是{},vm_name[]')
        # '''页面截图'''
        text = '''
        screenshot:%s,
        value['check']:%s,
        vm_name[%s]:%s
        ''' %(vm_name,value["check"],username,vm_name[username])
        if value["check"] in vm_name[username]:
            self.driver.get_screenshot_as_file(r"%s%s_success.png" %(value["screenshot_url"],username))
        else:
            self.driver.get_screenshot_as_file(r"%s%s__fail.png" %(value["screenshot_url"],username))
        return self.driver

    def find_clicks_script(self,locator,value="",username=""):
        '''在规定时长内查找元素，待元素可用后，'''
        self.find_clilk(locator,value['time_out'])
        return self.driver

    def iframe_switch_find_script(self,locator,value="",username=""):
        '''等待设置的时长后切换至对应ifranme并查看某元素是否存在，若存在则执行点击操作'''
        time.sleep(int(value["time_out"]))
        i = 0
        while True:
            try:
                self.to_iframe_xpath_script(locator,value)
                loca = (value["types"],value["values"])
                self.click(loca)
                break
            except Exception as e:
                i = i+1
                self.driver.switch_to.default_content()
                time.sleep(3)
        return self.driver

    def timing_execution_script(self,locator,value="",username=""):
        '''等待至规定时间'''
        import datetime,time
        global start_time
        global over_time
        if len(value["send_value"]) > 10:
            dateTime_p = datetime.datetime.strptime(value['send_value'],'%Y-%m-%d %H:%M:%S')
        else:
            if value["types"] == "start":
                dateTime_p = datetime.datetime.strptime(start_time,'%Y-%m-%d %H:%M:%S')
            else:
                dateTime_p = datetime.datetime.strptime(over_time,'%Y-%m-%d %H:%M:%S')
        now_time = datetime.datetime.now()
        while dateTime_p > now_time:
            time.sleep(1)
            now_time = datetime.datetime.now()
        return self.driver

    def key_fx_script(self,locator,value="",username=""):
        '''执行页面F12操作'''
        builder = ActionChains(self.driver)
        builder.key_down(Keys.F12).perform()
        return self.driver

    def data_clear_script(self,loctor,value="",username=""):
        '''数据清理'''
        config_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        delDir = os.path.join(config_path,'data')
        delList = os.listdir(delDir)
        for f in delList:
          filePath = os.path.join( delDir, f )
          if f == "data.xls":
              os.remove(filePath)
        return self.driver

    def batch_create_vm_script(self,locator,value="",username=""):
        '''批量创建接入点'''

        for i in range(2,int(value["send_value"])+2):
            search_for_elements = value["values"]
            wait_click_elements = value["value"]

            search_locator= (value["type"],search_for_elements.replace("flag","%d" %i))
            wait_click_locator = (value["types"],wait_click_elements.replace("flag","%d" %i))
            # print(search_locator,wait_click_locator)
            user_name = self.find(search_locator).text
            vm_name = ("%s_日志_vm_test" %user_name)

            self.click(wait_click_locator)  #点击配置接入点
            vm_locator = ('xpath',".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[7]/div[2]/div[1]/div/label[2]/span/input")
            self.click(vm_locator)  #选中接入方式为:vm
            time.sleep(1)
            add_vm_locator = ('xpath',".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[7]/div[2]/div[3]/div[2]")
            self.click(add_vm_locator)  #点击"添加一台虚拟机"按钮
            send_vm_name_locator = ('xpath',".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[14]/div[2]/div[1]/input")
            self.send(send_vm_name_locator,vm_name) #输入虚机名称
            select_locator = ('xpath',".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[14]/div[2]/div[2]/select")
            self.select(select_locator,"index","1")   #选择接入的交换机点
            time.sleep(2)
            select_2_locator = ('xpath','//*[@id="main"]/div/div[3]/div/div/div/div/div/div/div[14]/div[2]/div[3]/select')

            # self.select(select_2_locator,"index","174")  #win7_克隆_克隆
            self.select(select_2_locator,"index","12")   #选中镜像win7_日志虚机
            time.sleep(0.5)
            click_determine_button = ('xpath',".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[14]/div[3]/input[1]")
            print("正在为用户%s创建接入点：%s" %(user_name,vm_name),time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            self.click(click_determine_button)  #点击确定按钮
            time.sleep(0.5)
            success_locator = ('xpath',"html/body/div[12]/div/div/div[1]/div/span")
            result = self.find(success_locator,time_out="600").text
            if result == "成功":
                print("用户%s接入点：%s创建完成！" %(user_name,vm_name),time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                time.sleep(1)
                user_name = ""
            else:
                print("用户%s接入点：创建失败！提示信息为：%s" %(user_name,result))
                user_name = ""

    def batch_create_vm_log_script(self,locator,value="",username=""):
        '''批量创建接入点'''
        vm_list = [{'name': 'centos7.5', 'index': 13},
                   {'name': 'kali-19.1', 'index': 17},
                   {'name': 'ubuntu16.04-server', 'index': 29},
                   {'name': 'ubuntu18.04-server', 'index': 30},
                   {'name': 'win7_克隆_勿删', 'index': 34},
                   {'name': 'windows10', 'index': 38},
                   {'name': 'windows7-64', 'index': 39},
                   {'name': 'windowsserver2012', 'index': 41},
                   {'name': 'windowsserver2016', 'index': 42},
                   {'name': 'windowsserver2019', 'index': 43},
                   {'name': '克隆tk-mysql-15.1-opencart', 'index': 46},
                   {'name': '克隆tk-mysql-15.1-phpbb', 'index': 47},
                   {'name': '克隆tk-mysql-15.1-wordpress', 'index': 48},
                   {'name': '克隆tk-mysql-15.1-zencart', 'index': 49},
                   {'name': '克隆tk-mysql-slave-15.1-phpbb', 'index': 50},
                   {'name': '克隆tk-mysql-slave-15.1-wordpress', 'index': 51},
                   {'name': '克隆tk-nginx-15.1-opencart', 'index': 52},
                   {'name': '克隆tk-nginx-15.1-wordpress', 'index': 53},
                   {'name': '克隆tk-nginx-15.1-zencart', 'index': 54}]
        for i in range(len(vm_list)):
            search_for_elements = value["values"]
            wait_click_elements = value["value"]

            search_locator= (value["type"],search_for_elements.replace("flag","%d" %(i+2)))
            wait_click_locator = (value["types"],wait_click_elements.replace("flag","%d" %(i+2)))

            # print(search_locator,wait_click_locator)
            user_name = self.find(search_locator).text
            vm_name = ("%s_%s" %(user_name,vm_list[i]["name"]))

            self.click(wait_click_locator)  #点击配置接入点
            vm_locator = ('xpath',".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[7]/div[2]/div[1]/div/label[2]/span/input")
            self.click(vm_locator)  #选中接入方式为:vm
            time.sleep(3)
            add_vm_locator = ('xpath',".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[7]/div[2]/div[3]/div[2]")
            self.click(add_vm_locator)  #点击"添加一台虚拟机"按钮
            send_vm_name_locator = ('xpath',".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[14]/div[2]/div[1]/input")
            self.send(send_vm_name_locator,vm_name) #输入虚机名称
            select_locator = ('xpath',".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[14]/div[2]/div[2]/select")
            self.select(select_locator,"index","1")   #选择接入的交换机点
            time.sleep(2)
            select_2_locator = ('xpath','//*[@id="main"]/div/div[3]/div/div/div/div/div/div/div[14]/div[2]/div[3]/select')

            # self.select(select_2_locator,"index","174")  #win7_克隆_克隆
            self.select(select_2_locator,"index","%d"%vm_list[i]["index"])   #选中镜像win7_日志虚机
            time.sleep(0.5)
            click_determine_button = ('xpath',".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[14]/div[3]/input[1]")
            print("正在为用户%s创建接入点：%s" %(user_name,vm_name),time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            self.click(click_determine_button)  #点击确定按钮
            time.sleep(0.5)
            success_locator = ('xpath',"html/body/div[11]/div/div")

            result = self.find(success_locator,time_out="600").text
            if result == "成功":
                print("用户%s接入点：%s创建完成！" %(user_name,vm_name),time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                time.sleep(5)
            else:
                print("用户%s接入点：创建失败！提示信息为：%s" %(user_name,result))

    def canvas_move_click_script(self,locator,value="",username=""):
        x = int(value["types"])
        y = int(value["values"])
        print(x,y)
        canvas = self.find(locator)
        ActionChains(self.driver).move_to_element(canvas).move_by_offset(x,y).context_click().perform()
        # ActionChains(self.driver).move_to_element(canvas).move_by_offset(x,y).pause(2).click().perform()

if __name__ == "__main__":
    # config_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # delDir = os.path.join(config_path,'data')
    # delList = []
    # delList = os.listdir(delDir)
    # for f in delList:
    #     filePath = os.path.join( delDir, f )
    #     if f == "data.xls":
    #         os.remove(filePath)
    driver = webdriver.Chrome()
    driver.get("https://192.168.50.66")
    s = Script_value(driver)
    locator = ("xpath","")
    s.is_element_exist_click_plus_script()