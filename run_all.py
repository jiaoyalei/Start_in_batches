from case.Cze_Elective import demo
import time,sys,os


rootpath=str("E:\project\Start_in_batches")
syspath=sys.path
sys.path=[]
sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0]!="."])#将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)
print("开始执行！")
d = demo()
for i in range(1):
    print(i)
    d.login(i)
    time.sleep(5)