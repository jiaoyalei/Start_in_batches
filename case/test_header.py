# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get("http://www.baidu.com")
# value = driver.find_element_by_id("su")
# data = value.get_attribute("value")
# print(data)
# from common.read_excel import ExcelUtil
# import os
# real_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# data_path = os.path.join(os.path.join(real_path,"data"),"script_data.xls") #获取数据文件路径
# exce_data = ExcelUtil(data_path,'wait_time')
# date = exce_data.dict_data()
# print(date[0]['time'])

#wait_time: 2020-2-27 15:00:00
import os

delDir = "E:\BaiduNetdiskDownload\Start_in_batches\data"
delList = os.listdir(delDir )
for i in delList:
    print(i)
for f in delList:
  filePath = os.path.join( delDir, f )
  print(filePath)
  if f == "script_data(1).xls":
      os.remove(filePath)