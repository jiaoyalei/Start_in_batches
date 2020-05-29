import time
from common.script_value import Script_value
from common.logger import Log
import os,traceback



class Script_Case():
    #界面操作执行类'''
    def __init__(self,driver,username,time_data=""):
        self.time_data = time_data
        self.driver = driver
        self.username = username
        self.script_value = Script_value(self.driver,self.time_data)
        self.log = Log()

    def clear_data(self):
       config_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
       delDir = os.path.join(config_path,'data')
       delList = os.listdir(delDir)
       for f in delList:
        filePath = os.path.join( delDir, f )
        if f == "wait_time.xls":
            os.remove(filePath)

    def script_case(self,data):
      #将页面执行的操作类型存于字典中，进行对应操作函数的调用
       script_type = {
                      'click':self.script_value.click_script,                       #单击操作
                      'is_element_exis_and_click':self.script_value.is_element_exist_and_click_script,#查找元素，若元素存在则点击该元素
                      'to_iframe':self.script_value.to_iframe,                      #切换至iframe（名称定位）
                      'send':self.script_value.send_script,                         #填写操作
                      'time':self.script_value.time_script,                         #时间等待
                      'move':self.script_value.move_script,                         #鼠标悬停
                      'switch_content':self.script_value.switch_content_script,     #由iframe返回至页面顶层
                      'execution_script':self.script_value.execution_script_forto,  #js操作，滑动至页面底部
                      'window_handles':self.script_value.window_handles_script,     #页面跳转（跳转至最新弹出页面）
                      'to_iframe_xpath':self.script_value.to_iframe_xpath_script,   #切换至iframe（xpath定位）
                      'move_perform':self.script_value.move_perform_script,         #鼠标移动至指定位置进行右键操作
                      'move_perform_click':self.script_value.move_perform_click_script,  #鼠标移动至指定位置进行单击操作
                      'get_text':self.script_value.get_text_script,      #获取元素文本信息（此函数通过文本信息进行开机状态判断）
                      'text_in_element':self.script_value.text_in_element_script,   #判断页面文本元素是否存在，并将结果存入全局变量
                      'baidu_demo':self.script_value.baidu_demo_script,      #demo
                      'refresh':self.script_value.refresh_script,            #刷新页面操作
                      'drag_element':self.script_value.drag_element_script,  #将页面元素向右拖拽
                      'drag_and_drop':self.script_value.drag_and_drop,       #将页面元素向指定位置拖拽（均通过元素定位）
                      'select':self.script_value.select_script,              #页面下拉框操作，可按value、index、文本三种定位方式
                      'screenshot':self.script_value.screenshot_script,      #页面截图
                      'multiple_clicks':self.script_value.find_clicks_script,            #等待元素可用后，进行单击操作
                      'iframe_switch_find':self.script_value.iframe_switch_find_script,  #进行时间等待后，切换到iframe中，由iframe中查找元素，并单击
                      'timing_execution':self.script_value.timing_execution_script,      #等待至固定时间，用于业务并发
                      'get_vm_state':self.script_value.get_vm_state_script,              #获取虚机开机状态，并进行虚机开机判断
                      'key_fx':self.script_value.key_fx_script,                          #执行键盘操作：F12
                      'data_clear':self.script_value.data_clear_script,                  #数据清理
                      'script_js':self.script_value.script_js_forto,                     #js操作，进行指定大小滑动
                      'send_random':self.script_value.send_random_script,                #填写不可重名数据（名称后编号自动增涨）
                      'click_random':self.script_value.click_random_script,              #进行页面随机单击操作，用于场景关联时，选择不同场景
                      'get_czx_vm_state':self.script_value.get_czx_vm_state_script,      #CZX获取虚机开机状态，并进行虚机开机判断
                      'is_element_exist_click':self.script_value.is_element_exist_click_script,     #等待指定页面元素出现后，点击某元素
                      'is_element_exist_plus':self.script_value.is_element_exist_click_plus_script, #通过验证某元素信息文本内容，点击其下对应元素
                                                                                                    #（用于指定修改或执行某特定任务）
                      'get_text_and_status':self.script_value.get_text_and_status_script,  #每5秒进行一次页面文本获取（用于CZE虚机多少秒内开机）
                      'batch_create_vm':self.script_value.batch_create_vm_script,          #czx批量创建接入点VM
                      'canvas_move_click':self.script_value.canvas_move_click_script,       #画布对应操作（暂不可用）
                      'batch_create_vm_log':self.script_value.batch_create_vm_log_script
                      }
       for value in data:
           try:
               self.log.info("%s:%s" %(self.username,value["notes"]))
               # if value['execution_type'] == "timing_execution":
               #     print("%s：已准备就绪，%s开始执行！"%(self.username,value["send_value"]))
               loca = (value["type"],value["value"])   #获取元素操作的元素定位方式及定位值
               self.driver = script_type[value['execution_type']](loca,value,self.username)#调用操作函数

           except Exception:
               error = traceback.format_exc()
               self.log.error("%s:【%s】" %(self.username,value["notes"])+error)
       self.clear_data()
       return self.driver