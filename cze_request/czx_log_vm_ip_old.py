import requests,time,collections
requests.packages.urllib3.disable_warnings()

task_id = "logstash_applicationlog-b0552a2d798a426a8c343e8abe7ae2b9"
author_token = "Bearer 73a98ce7-82f2-484d-a9a8-402cc7f61050"

headers = {"Authorization":"%s" %author_token}  #接口验证信息
params = {"index":"%s" %task_id,"rows":1000,"pageSize":1}   #index为任务标识ID，rows为查询多少条数据logstash_applicationlog-32a862d6e5da441c9214abef7ad46372
re = requests.post("https://192.168.50.65/api/applicationLog_es/v1/applicationLog/findAllApplicationLogByPage",headers=headers,verify=False,params=params)


data = re.json() #获取接口返回数据
vm_list = data["data"]["data"]   #获取ip数据
count = data["data"]["totalSize"]
print("接口返回总条数：%d，实际总条数:%d"%(count,len(vm_list)))
vm_list_all = []
vm_list_ip = []
#ip去重
for i in range(len(vm_list)):
    # print(vm_list[i]["ipAddress"],i+1)
    vm_list_all.append(vm_list[i]["ipAddress"])
    if vm_list[i]["ipAddress"] not in vm_list_ip:
        vm_list_ip.append(vm_list[i]["ipAddress"])
print("共%d台,%s" %(len(vm_list_ip),vm_list_ip))
dic = collections.Counter(vm_list_all)
sum_value = 0
for key in dic:
    print("%s共发送->%d条日志" %(key,dic[key]))
    sum_value = sum_value + dic[key]
print(sum_value)

