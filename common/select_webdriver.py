from selenium import webdriver
import time

class Select_Webdriver():
    '''浏览器类别与运行模式类'''
    def __init__(self,type="",head_type="",developer_debug_pattern=False):

        self.type = type
        self.head_type = head_type
        self.developer_debug = developer_debug_pattern
        if head_type == "no-head":
            self.chrome_options = webdriver.ChromeOptions()
            #self.options.add_argument("--auto-open-devtools-for-tabs")   #开启浏览器开发者工具
            self.chrome_options.add_argument('headless')   #开启浏览器无头模式
            self.firefox_options = webdriver.FirefoxOptions()
            self.firefox_options.add_argument('-headless')

    def chrome(self):
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        return self.driver

    def firefox(self):
        self.driver = webdriver.Firefox(firefox_options=self.firefox_options)
        return self.driver

    def webdriver_open(self):
        if self.type == "Chrome" and self.head_type=="no-head":
           self.driver = self.chrome()
           self.driver.maximize_window()
        elif self.type == "Firefox" and self.head_type=="no-head":
           self.driver = self.firefox()
           self.driver.maximize_window()
        elif self.type == "Chrome":
            if self.developer_debug == True:
            # self.chrome_options = webdriver.ChromeOptions()
            # self.chrome_options.add_argument(r'user-data-dir=C:/Users/safecode/AppData/Local/Google/Chrome/User Data')
            # self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
                options = webdriver.ChromeOptions()
                options.add_argument("--auto-open-devtools-for-tabs")
                self.driver = webdriver.Chrome(chrome_options=options)
                self.driver.maximize_window()
            else:
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
        elif self.type == "Firefox":
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        return self.driver




if __name__ == "__main__":
    sele_driver = Select_Webdriver("Chrome",developer_debug_pattern=True).webdriver_open()
    sele_driver.get("http://www.baidu.com")
    print(sele_driver.title)
    time.sleep(3)
    sele_driver.quit()