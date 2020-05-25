import os
import random          #导入 random(随机数) 模块
import time

from PIL import Image
from Verification_Code.baidu_ocr import BaiDu_cor
from selenium import webdriver
from Verification_Code.yzm_jiangzao import pictureIdenti
from Verification_Code.jiangzao import one_value,three_value,two_value,four_value


class Yzm_get(object):
    '''验证码获取类'''
    def __init__(self,driver):
        self.driver = driver

    def file_delete(self,del_file):
        ls = os.listdir(del_file)
        for i in ls:
            c_path = os.path.join(del_file, i)
            if os.path.isdir(c_path):
                self.file_delete(c_path)
            else:
                os.remove(c_path)

    #截图，裁剪图片并返回验证码图片名称
    # _save_url 保存路径 ；yuansu 验证码元素标识
    def yzm_text_get(self,save_url=r"C:\Users\safecode\Desktop\image",yuansu=".//*[@id='main']/div/div/div[2]/form/div[4]/div/img",value=1):
        # try:
            file_name = random.randint(0, 100000)
            file_name_wz =r'\%s.png' %str(file_name)
            file_url = save_url + file_name_wz
            self.driver.get_screenshot_as_file(file_url)  # get_screenshot_as_file截屏
            captchaElem = self.driver.find_element_by_xpath(yuansu)  # # 获取指定元素（验证码）
            # 因为验证码在没有缩放，直接取验证码图片的绝对坐标;这个坐标是相对于它所属的div的，而不是整个可视区域
            # location_once_scrolled_into_view 拿到的是相对于可视区域的坐标  ;  location 拿到的是相对整个html页面的坐标
            captchaX = int(captchaElem.location['x'])
            captchaY = int(captchaElem.location['y'])

            # 获取验证码宽高
            captchaWidth = captchaElem.size['width']
            captchaHeight = captchaElem.size['height']


            captchaRight = captchaX + captchaWidth
            captchaBottom = captchaY + captchaHeight

            imgObject = Image.open(file_url)  #获得截屏的图片
            imgCaptcha = imgObject.crop((captchaX, captchaY, captchaRight, captchaBottom))  # 裁剪
            yanzhengma_file_name = save_url+'\yzm\%dfuben.png' %(value)
            imgCaptcha.save(yanzhengma_file_name)
            two_value(save_url)
            one_value(save_url)
            three_value(save_url)
            four_value(save_url)
            # image_jz = pictureIdenti().clearNoise(img_name=yanzhengma_file_name)
            image_text = BaiDu_cor().yzm_text(save_url+r'\yzm2\xiufu.png')
            # print("验证码内容：",image_text)
            self.file_delete(save_url)
            return image_text








if __name__ == "__main__":
    image_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    image_url = os.path.join(image_path,'image')
    driver = webdriver.Chrome()
    driver.get("http://192.168.50.66")
    driver.maximize_window()

    driver.find_element_by_xpath(".//*[@id='main']/div/div/div[2]/form/div[2]/div/div[1]/input").send_keys("test_student")
    driver.find_element_by_xpath(".//*[@id='main']/div/div/div[2]/form/div[3]/div/div/input").send_keys("qaz123456")
    image_demo = Yzm_get(driver)
    text = image_demo.yzm_text_get(image_url)
    driver.find_element_by_xpath(".//*[@id='main']/div/div/div[2]/form/div[4]/div/div[1]/input").send_keys(text)
    driver.find_element_by_xpath(".//*[@id='main']/div/div/div[2]/form/div[5]/div/button").click()
    time.sleep(2)

    falg = True
    while falg:
        try:
            driver.find_element_by_xpath(".//*[@id='main']/div/div[1]/div/div[3]/div/div[1]/a")
            falg = False
        except Exception as e:
            time.sleep(0.5)
            # driver.find_element_by_xpath(".//*[@id='main']/div/div/div/form/div[3]/div/img").click()
            driver.find_element_by_xpath(".//*[@id='main']/div/div/div[2]/form/div[4]/div/div[1]/input").clear()
            time.sleep(0.5)

            text = image_demo.yzm_text_get(image_url)
            driver.find_element_by_xpath(".//*[@id='main']/div/div/div[2]/form/div[4]/div/div[1]/input").send_keys(text)
            driver.find_element_by_xpath(".//*[@id='main']/div/div/div[2]/form/div[5]/div/button").click()
            time.sleep(1.5)
    time.sleep(3)
    driver.close()
    driver.quit()


