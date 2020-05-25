import unittest,ddt,time,os
from selenium import webdriver
from common.common_rwcd import Common_Read as cr
from common.base import Base

real_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(os.path.join(real_path,"data"),"czx_user.xls")
data = cr(data_path,'user').dict_data()



@ddt.ddt
class TestAddUser(unittest.TestCase):
    '''批量添加用户类'''
    @classmethod
    def setUpClass(cls,username="gongan",password="qaz123456"):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://192.168.50.65")
        cls.b = Base(cls.driver)
        loca = ("xpath",".//*[@id='main']/div/div/div[2]/form/div[2]/div/div/input")
        cls.b.send(loca,username)
        loca2 = ("xpath",".//*[@id='main']/div/div/div[2]/form/div[3]/div/div/input")
        cls.b.send(loca2,password)
        time.sleep(5)
        loca3 = ("xpath",".//*[@id='main']/div/div/div[2]/form/div[5]/div/button")
        cls.b.click(loca3)
        time.sleep(3)
        loca4 = ("xpath",".//*[@id='main']/div/div[1]/div/div[2]/div/ul/li[2]/div[1]")
        cls.b.move(loca4)
        time.sleep(1)
        loca5 = ("xpath",".//*[@id='main']/div/div[1]/div/div[2]/div/ul/li[2]/div[2]/ul/li[1]")
        cls.b.click(loca5)


    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()

    @ddt.data(*data)
    def test_add_user(self,data):
        time.sleep(1)
        print(data)
        loca6 = ("xpath",".//*[@id='main']/div/div[3]/div/div/div/div/div/div/div[1]/a[4]")
        self.b.click(loca6)
        loca7 = ("xpath",".//*[@id='main']/div/div[3]/div/div/div/div/div[1]/div/form/div[1]/div/div[1]/input")
        self.b.send(loca7,data["username"])
        loca8 = ("xpath",".//*[@id='main']/div/div[3]/div/div/div/div/div[1]/div/form/div[2]/div/div[1]/div/input")
        self.b.send(loca8,data["password"])
        loca9 = ("xpath",".//*[@id='main']/div/div[3]/div/div/div/div/div[1]/div/form/div[3]/div/div/div/input")
        self.b.send(loca9,data["password"])
        loca10 = ("xpath",".//*[@id='main']/div/div[3]/div/div/div/div/div[1]/div/form/div[4]/div/div[1]/input")
        self.b.send(loca10,data["accountnumber"])
        loca11 = ("xpath",".//*[@id='main']/div/div[3]/div/div/div/div/div[1]/div/form/div[6]/div/div[1]/input")
        self.b.send(loca11,data["phone"])
        loca12 = ("xpath",".//*[@id='main']/div/div[3]/div/div/div/div/div[1]/div/form/div[7]/div/div[1]/input")
        self.b.send(loca12,data["email"])
        self.b.execution_script()
        loca13 = ("xpath",".//*[@id='main']/div/div[3]/div/div/div/div/div[1]/div/form/div[11]/div/div[1]/div/div[1]/div/span")
        self.b.click(loca13)
        loca14 = ("xpath",".//*[@id='main']/div/div[3]/div/div/div/div/div[1]/div/form/div[11]/div/div[1]/div/div[2]/ul[2]/li[6]")
        self.b.click(loca14)
        loca15 = ("xpath",".//*[@id='main']/div/div[3]/div/div/div/div/div[2]/button[2]")
        self.b.click(loca15)
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()