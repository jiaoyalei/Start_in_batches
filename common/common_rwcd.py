import yaml,os,xlrd,random,datetime,xlwt
from xlutils.copy import copy
import openpyxl




class Common_Read():
    def __init__(self, excelPath="", sheetName="Sheet1"):
        if excelPath !="":
            self.data = xlrd.open_workbook(excelPath)
            self.table = self.data.sheet_by_name(sheetName)
            # 获取第一行作为key值
            self.keys = self.table.row_values(0)
            # 获取总行数
            self.rowNum = self.table.nrows
            # 获取总列数
            self.colNum = self.table.ncols

    def get_config_data(self,key_value):
        config_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        yamlpath= os.path.join(os.path.join(config_path,'conf'),'config.yaml')
        f = open(yamlpath,'r',encoding='utf-8')
        cfg = f.read()
        data = yaml.load(cfg,Loader=yaml.FullLoader) # yaml 5.1版本后弃用了yaml.load(file)这个用法，
                                               # 因为觉得很不安全，5.1版本之后就修改了需要指定L
                                                    # oader，通过默认加载装饰器（FullLoader）禁止执行任意函数
        return data[key_value]

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            for k in r:
                try:
                    if k['execution_type'] == "click_random":
                        if k['types'] == "task":
                            random_value = random.randint(1,int(k['send_value']))
                            k['value'] = ".//*[@id='main']/div/div[3]/div/div/div/div[1]/di" \
                                     "v/div/div[2]/div/div[4]/div[1]/div/div/div[2]/tab" \
                                     "le/tbody/tr[%d]/td[1]/div/div/label/span/input" %(random_value)
                        else:
                            random_value = random.randint(1,int(k['send_value']))
                            k['value'] = ".//*[@id='main']/div/div[3]/div/div/div/div/div[1]" \
                                         "/div/form/div[4]/div/div[1]/div[2]/ul[2]/li[%d]" %(random_value)
                except Exception as e:
                    pass
            return r

    def base_dir(self,filename=None):
        '''获取data.xls的存在路径'''
        real_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(os.path.join(real_path,"data"),filename)
        return data_path


    def add_waittime_excel(self):
        """对excel进行修改/添加内容"""
        start_interval,over_interval = self.get_config_data('start_interval'),self.get_config_data('over_interval')
        real_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(os.path.join(real_path,"data"),"wait_time.xls")
        start_time = ((datetime.datetime.now() + datetime.timedelta(minutes=start_interval)).strftime("%Y-%m-%d %H:%M:%S"))
        over_time = ((datetime.datetime.now() + datetime.timedelta(minutes=(start_interval+over_interval))).strftime("%Y-%m-%d %H:%M:%S"))
        wb = xlwt.Workbook()
        sht1 = wb.add_sheet("wait_time")
        sht1.write(0,0,'start_time')
        sht1.write(0,1,'over_time')
        sht1.write(1,0,start_time)
        sht1.write(1,1,over_time)

        wb.save(data_path)






    def clear_screenshot(self,delDir):
        delList = os.listdir(delDir)
        for f in delList:
          filePath = os.path.join(delDir, f )
          if "png" in filePath:
            os.remove(filePath)

if __name__ == "__main__":
    # driver = webdriver.Chrome()
    # driver.get("https://192.168.50.116")
    # b = Base(driver)
    filepath = r"E:\project\Start_in_batches\data\czx_data.xls"
    sheetName = "czx_new_scene"
    data = Common_Read(filepath, sheetName)
    data_value = data.dict_data()
    for i in data_value:
        print(i)
    # data2 = data.dict_data()
    # print(data2)
    # Common_Read().write_copy()
    # (Common_Read().get_config_data("test_url"))
    # Common_Read().add_waittime_excel()



