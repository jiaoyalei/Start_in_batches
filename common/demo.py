
# from selenium import webdriver
# import time
# from common.logger import Log
# from common.base import Base
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
#
# log = Log()
# driver = webdriver.Chrome()
# driver.maximize_window()
# b = Base(driver)
# # driver.get("https://www.baidu.com")
# driver.get("https://192.168.235.143")
# driver.find_element_by_xpath(".//*[@id='login']/div/div[2]/form/div[1]/div/div[1]/input").send_keys("test_student81")
# driver.find_element_by_xpath(".//*[@id='login']/div/div[2]/form/div[2]/div/div/input").send_keys("Safecode@123")
# driver.find_element_by_xpath(".//*[@id='login']/div/div[2]/div[1]").click()
# time.sleep(3)
# driver.find_element_by_xpath(".//*[@id='app']/div/div[1]/div/div[2]/ul/li[2]").click()
# time.sleep(3)
# driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/div/div[2]/div/div[2]/div[1]/span[1]/img").click()
# time.sleep(3)
# driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/div/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[7]/div/div/div").click()
# n = driver.window_handles # 获取当前页句柄
# print(n)
# driver.switch_to.window (n[-1]) # 切换到新的网页窗口
# # driver.find_element_by_xpath(".//*[@id='app']/div/div[1]/div[2]/div/div/span[3]").click()
# # time.sleep(1)
# # element = driver.find_element_by_xpath("html/body/div/div/div[2]/div[2]/iframe")
# # driver.switch_to.frame(element)
# # time.sleep(3)
# # text_result = driver.find_element_by_xpath(".//*[@id='status']").text
# # if "Connected to" in text_result:
# #     print("5秒内开机成功！")
# #
# #
# #
# # import os
# # import sys
# # rootpath=str("E:\project\Start_in_batches")
# # syspath=sys.path
# # sys.path=[]
# # sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
# # sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0]!="."])#将工程目录下的一级目录添加到python搜索路径中
# # sys.path.extend(syspath)
# c = []
# a = 'abcde'
# b = ['a','b']
# c.append(a)
# #['abcde]
# c.append(b)
# # print(c)
# a=input("Please enter a sentence, each word is separated by spaces : ")
# b=a.split(" ")
#
# max_word=0
# max_index=0
# for i in range(len(b)-1):
#     if len(b[i])>len(b[i+1]):
#         max_word=b[i]
#         max_index=i+1
#     c=[max_word]
#     c.append(max_index)
# print(c)
# username1 = "adb"
# text = "heihei"
# username = "adb"
#
# vm_value = {}
# vm_value.update(eval("{'%s':'%s'}" %(username,text)))
# vm_value.update(eval("{'%s':'开机超时或虚机未开启！'}" %(username)))
# for i in vm_value:
#     print(i,":",vm_value[i])

#
# print("用户：%s-->5秒内开机结果为:%s" %(username,vm_value[username]))
# vm_value.update(t)
# vm_value.update({"username2":"heihei2"})
# print(vm_value)
# data1 = [{'type': 'xpath', 'value': ".//*[@id='main']/div/div[1]/div/div[2]/div/ul/li[3]/div[1]", 'execution_type': 'move', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"网络演训"'}, {'type': 'xpath', 'value': "//*[text()='模拟演练']", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"模拟演练"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div[1]/div/div/div/div[1]/a", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"新建任务"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[1]/div/div[1]/input", 'execution_type': 'send_random', 'send_value': '压力测试任务创建', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入任务名称'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[2]/div/div/input", 'execution_type': 'send', 'send_value': '移动5G', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入任务标签'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[3]/div/div[1]/textarea", 'execution_type': 'send', 'send_value': '暂无描述', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入任务描述'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[4]/div/div/div[1]/input", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '选中日志监控'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[4]/div/div/div[2]/input", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '选中全程录屏'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[4]/div/div/div[3]/input", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '选中同屏监控'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[5]/div/div/label[2]/span/input", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '选中手动控制 '}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[2]/ul/li[2]/button", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"场景配置"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/div[3]/div[2]/img", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"场景关联"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/div[2]/div/div[4]/div[1]/div/div/div[2]/table/tbody/tr[flag]/td[1]/div/div/label/span/input", 'execution_type': 'is_element_exist_plus', 'send_value': '', 'types': 'xpath', 'values': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/div[2]/div/div[4]/div[1]/div/div/div[2]/table/tbody/tr[flag]/td[4]/div/span", 'time_out': '', 'check': ' 日志压力测试场景 ', 'screenshot_url': '', 'notes': '选中"场景"'}, {'type': '', 'value': '', 'execution_type': 'timing_execution', 'send_value': '2020-4-1 11:32:00', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '固定时间执行下一步'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[3]/ul/li[2]/button", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"接入配置"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/div[3]/button", 'execution_type': 'is_element_exis_and_click', 'send_value': '', 'types': '', 'values': '', 'time_out': 900.0, 'check': '', 'screenshot_url': '', 'notes': '10分钟中内查找新建分组按钮，并单击'}, {'type': 'xpath', 'value': 'html/body/div[13]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input', 'execution_type': 'send', 'send_value': '经典蓝方', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入分组名称'}, {'type': 'xpath', 'value': 'html/body/div[13]/div[2]/div/div/div[2]/form/div[5]/div/div/textarea', 'execution_type': 'send', 'send_value': '暂无说明 ', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入任务说明 '}, {'type': 'xpath', 'value': 'html/body/div[13]/div[2]/div/div/div[3]/div/button[1]', 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"保存"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/div[4]/div/div[2]/table/tbody/tr/td[7]/div/div/a[3]", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"添加执行人"'}, {'type': 'xpath', 'value': 'html/body/div[14]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/div/label/span/input', 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '添加第一位学生'}, {'type': 'xpath', 'value': 'html/body/div[14]/div[2]/div/div/div[2]/div/div[1]/div[2]/button', 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"添加"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/div[4]/div/div[2]/table/tbody/tr/td[7]/div/div/a[4]", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"详情配置"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[3]/div[2]/div/div[3]/input[3]", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"配置接入点"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[7]/div[2]/div[2]/div[1]/input[1]", 'execution_type': 'send', 'send_value': '探险', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入ip'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[7]/div[2]/div[2]/div[1]/input[2]", 'execution_type': 'send', 'send_value': '完满', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入子网掩码'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[7]/div[2]/div[2]/div[1]/input[3]", 'execution_type': 'send', 'send_value': '结束', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入网关'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[7]/div[3]/input[1]", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击保存'}]
# for i in data1:
#     if (i["execution_type"]) == "is_element_exist_plus":
#         print(i)
#         data = i
# for i in range(1,11):
#     value = data["value"]
#     value3 = data["values"]
#     loca = (value,value3)
#     print(loca)
#     value2= value.replace("flag","%d" %i)
#     value4 = value3.replace("flag","%d" %i)
#     print(value2,value4)
# data = [{'type': 'xpath', 'value': ".//*[@id='main']/div/div[1]/div/div[2]/div/ul/li[3]/div[1]", 'execution_type': 'move', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"网络演训"'}, {'type': 'xpath', 'value': "//*[text()='模拟演练']", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"模拟演练"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div[1]/div/div/div/div[1]/a", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"新建任务"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[1]/div/div[1]/input", 'execution_type': 'send_random', 'send_value': '压力测试任务创建', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入任务名称'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[2]/div/div/input", 'execution_type': 'send', 'send_value': '移动5G', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入任务标签'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[3]/div/div[1]/textarea", 'execution_type': 'send', 'send_value': '暂无描述', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入任务描述'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[4]/div/div/div[1]/input", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '选中日志监控'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[4]/div/div/div[2]/input", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '选中全程录屏'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[4]/div/div/div[3]/input", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '选中同屏监控'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/form/div[5]/div/div/label[2]/span/input", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '选中手动控制 '}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[2]/ul/li[2]/button", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"场景配置"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/div[3]/div[2]/img", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"场景关联"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/div[2]/div/div[4]/div[1]/div/div/div[2]/table/tbody/tr[flag]/td[1]/div/div/label/span/input", 'execution_type': 'click', 'send_value': '', 'types': 'xpath', 'values': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/div[2]/div/div[4]/div[1]/div/div/div[2]/table/tbody/tr[flag]/td[4]/div/span", 'time_out': '', 'check': ' 日志压力测试场景 ', 'screenshot_url': '', 'notes': '选中"场景"'}, {'type': '', 'value': '', 'execution_type': 'timing_execution', 'send_value': '2020-4-1 11:32:00', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '固定时间执行下一步'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[3]/ul/li[2]/button", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"接入配置"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/div[3]/button", 'execution_type': 'is_element_exis_and_click', 'send_value': '', 'types': '', 'values': '', 'time_out': 900.0, 'check': '', 'screenshot_url': '', 'notes': '10分钟中内查找新建分组按钮，并单击'}, {'type': 'xpath', 'value': 'html/body/div[13]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input', 'execution_type': 'send', 'send_value': '经典蓝方', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入分组名称'}, {'type': 'xpath', 'value': 'html/body/div[13]/div[2]/div/div/div[2]/form/div[5]/div/div/textarea', 'execution_type': 'send', 'send_value': '暂无说明 ', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入任务说明 '}, {'type': 'xpath', 'value': 'html/body/div[13]/div[2]/div/div/div[3]/div/button[1]', 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"保存"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/div[4]/div/div[2]/table/tbody/tr/td[7]/div/div/a[3]", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"添加执行人"'}, {'type': 'xpath', 'value': 'html/body/div[14]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/div/label/span/input', 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '添加第一位学生'}, {'type': 'xpath', 'value': 'html/body/div[14]/div[2]/div/div/div[2]/div/div[1]/div[2]/button', 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"添加"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div[1]/div/div/div[4]/div/div[2]/table/tbody/tr/td[7]/div/div/a[4]", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"详情配置"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[3]/div[2]/div/div[3]/input[3]", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击"配置接入点"'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[7]/div[2]/div[2]/div[1]/input[1]", 'execution_type': 'send', 'send_value': '探险', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入ip'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[7]/div[2]/div[2]/div[1]/input[2]", 'execution_type': 'send', 'send_value': '完满', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入子网掩码'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[7]/div[2]/div[2]/div[1]/input[3]", 'execution_type': 'send', 'send_value': '结束', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '输入网关'}, {'type': 'xpath', 'value': ".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[7]/div[3]/input[1]", 'execution_type': 'click', 'send_value': '', 'types': '', 'values': '', 'time_out': '', 'check': '', 'screenshot_url': '', 'notes': '点击保存'}]
# for i in data:
#     print(i)

# import time
#
#
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# import os,time
# import pyautogui as pag
# try:
#     while True:
#             print("Press Ctrl-C to end")
#             x,y = pag.position() #返回鼠标的坐标
#             print(x,y)
#             posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
#             print (posStr)#打印坐标
#             time.sleep(5)
#             os.system('cls')#清楚屏幕
# except  KeyboardInterrupt:
#     print ('end....')
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# def click_locxy(dr, x, y, left_click=True):
#     '''
#     dr:浏览器
#     x:页面x坐标
#     y:页面y坐标
#     left_click:True为鼠标左键点击，否则为右键点击
#     '''
#     if left_click:
#         ActionChains(dr).move_by_offset(x, y).click().perform()
#     else:
#         ActionChains(dr).move_by_offset(x, y).context_click().perform()
#     ActionChains(dr).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前
#
# if __name__ == "__main__":
#     dr = webdriver.Chrome()
#     dr.get('http://www.baidu.com')
#     dr.maximize_window()
#     # click_locxy(dr, 0, 0,left_click=False) # 左键点击
#     # time.sleep(3)
#     click_locxy(dr, 100, 100, left_click=False) # 右键点击
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.add_argument("--auto-open-devtools-for-tabs")
# driver = webdriver.Chrome(chrome_options=options)
# driver.maximize_window()
# driver.get("https://www.baidu.com")
#
import openpyxl,os,datetime

# # real_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # data_path = os.path.join(os.path.join(real_path,"data"),"data.xls") #获取数据文件路径
# # wb = openpyxl.Workbook()
# # wb.create_sheet("wait_time")
# # wb.save(data_path)
# base_dir = os.path.join("D:/","//report","//text.ini")
# print(base_dir)
# date1 = "2019-10-24"  #10 2 11 8 12 8 1 12
# date2 = "2020-1-10"
# date4 = "2020-4-3"
# date3 = "2020-5-11"
#
# date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
# date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
# date3 = datetime.datetime.strptime(date3, "%Y-%m-%d")
# date4 = datetime.datetime.strptime(date4, "%Y-%m-%d")
# print(date2-date1)
# print(date3-date4)
start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print(start_time,type(start_time))

time = {}
time2 = {"test_student":{"start_time":"2020-05-27 18:35:51","end_time":"2020-05-27 19:35:55"}}
start_time = datetime.datetime.strptime(time2["test_student"]["start_time"],'%Y-%m-%d %H:%M:%S')
end_time = datetime.datetime.strptime(time2["test_student"]["end_time"],'%Y-%m-%d %H:%M:%S')
print(start_time,end_time)
print(end_time-start_time)
