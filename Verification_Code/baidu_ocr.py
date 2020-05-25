from aip import AipOcr
import time

APP_ID = '17836575'
API_KEY = 'nHnl0XlF6nGAUFrGC9GDjsLa'
SECRECT_KEY = 'XMZmbvBKBXgBEn0OKE2cCFmVuS9ZHO4y'
client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)


class BaiDu_cor():

    def yzm_text(self,image_path):
            #定义参数变量
        options = {
            #定义图像方向
            'detect_direction':'true',
            #识别语文类型，默认为'CHN_ENG'
            'language_type':'CHN_ENG',
        }
        image = self.get_file_content(image_path)
        #调用通用文字识别 接口
        result = client.general(image,options)
        # result = client.basicAccurate(image)
        text = result['words_result']
        text_value = text[0]['words']
        text2 = text_value.replace(' ','')
        text3 = text2[0:4]

        # for word in result['words_result']:
        #     text = word['words']
        #     if text == "":
        #         text = 'None'
        #         return text
        #     else:
        #         m = ""
        #         for j in text:
        #             if j != "":
        #                 m = m + j
        return text3





    def get_file_content(self,filePath):
        with open(filePath,'rb') as fp:
            return fp.read()



    # #调用通用文字识别，图片参数为本地图片
    # result = client.general(image)


if __name__ == "__main__":
    image_text = BaiDu_cor().yzm_text(r'C:\Users\safecode\Desktop\image\yzm\three.png')
    print("验证码内容：",image_text)

