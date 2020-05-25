from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from common.logger import Log
from selenium.webdriver.common.keys import Keys




class Base():

    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver
        self.log = Log()

    def find(self, locator,time_out="5"):
        '''loctor = ("id", "kw")'''
        element = WebDriverWait(self.driver, int(time_out), 0.5).until(lambda x: x.find_element(*locator))
        return element

    def find_clilk(self,locator,time_out="3"):
        print("来到了find_clilk,time_out为:%s,locator为:%s" %(time_out,locator))
        # element = WebDriverWait(self.driver,int(time_out),0.5).until(EC.element_to_be_clickable(*locator))
        element = WebDriverWait(self.driver, int(time_out), 0.5).until(lambda x: x.find_element(*locator))
        element.click()
        return self.driver

    def finds(self, locator):
        '''loctor = ("id", "kw")'''
        elements = WebDriverWait(self.driver, 30, 0.5).until(lambda x: x.find_elements(*locator))
        return elements

    def element_find(self,locator):
        element = WebDriverWait(self.driver, 1800, 0.5).until(lambda x: x.find_element(*locator))
        return element

    def send(self, locator, _text):
        '''loctor = ("id", "kw")'''
        self.find(locator).send_keys(_text)

    def click(self, locator):
        self.find(locator).click()

    def execution_script(self):
        '''滑动至页面底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def is_element_exist(self, locator,time_out):
        try:
            self.find(locator,time_out)
            return True
        except:
            return False

    def text_in_element(self, locator, _text):
        try:
            r = WebDriverWait(self.driver, 3, 0.5).until(EC.text_to_be_present_in_element(locator, _text))
            return r
        except:
            return False

    def value_in_element(self, locator, _text):
        try:
             r = WebDriverWait(self.driver, 15, 1).until(EC.text_to_be_present_in_element_value(locator, _text))
             return r
        except:
             return False

    def move(self,locator):
        mouse = self.find(locator)
        ActionChains(self.driver).move_to_element(mouse).perform()

    def switch_to(self,ifame_name):
        self.driver.switch_to.frame(ifame_name)


    def select(self,locator,type,flag_value):
        s = self.find(locator)
        if type == "value":
            Select(s).select_by_value(flag_value)
        elif type == "index":
            Select(s).select_by_index(int(flag_value))
        else:
            Select(s).select_by_visible_text(flag_value)



if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://192.168.50.116")
    b = Base(driver)
    loca1 = ("xpath",".//*[@id='main']/div/div/div/form/div[1]/div/div/input")
    loca2 = ("xpath",".//*[@id='main']/div/div/div/form/div[2]/div/div/input")
    loca3 = ("xpath",".//*[@id='main']/div/div/div/form/div[3]/div/button")
    loca4 = ("xpath",".//*[@id='main']/div/div[1]/div[2]/div/div[2]/a")
    loca5 = ("xpath",".//*[@id='main']/div/div[1]/div[2]/div/div[1]/a")
    # 登录

    b.send(loca1,"test")

    b.send(loca2,"qaz123456")

    b.click(loca3)
    # text = b.find(loca5).text
    # print(text)
    flag = b.text_in_element(loca5,"test")
    print(flag)


    from selenium.webdriver.common.by import By

    # driver.find_element(By.ID, "id值")
    # driver.find_element("id", "id值")




























