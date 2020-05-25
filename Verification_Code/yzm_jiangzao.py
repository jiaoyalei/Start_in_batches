#coding:utf8
import os
from PIL import Image,ImageDraw,ImageFile
import numpy
import pytesseract

class pictureIdenti:
    # 点降噪
    def clearNoise(self, img_name=r"C:\Users\safecode\Desktop\yzm2\1_CL",value="", x=0, y=0):
        if os.path.exists(img_name):
            image = Image.open(img_name)
            image = image.convert('L')
            image = numpy.asarray(image)
            image = (image > 135) * 255
            image = Image.fromarray(image).convert('RGB')

            # image.show()
            save_name = r"C:\Users\safecode\Desktop\image\yzm2\1_CL.png"
            image.save(save_name)
            return image

if __name__ == "__main__":

    image_demo = pictureIdenti()
    for i in range(1,101):
        image_demo.clearNoise(img_name=r"C:\Users\safecode\Desktop\yzm\dfufen.png" %i,value=i)