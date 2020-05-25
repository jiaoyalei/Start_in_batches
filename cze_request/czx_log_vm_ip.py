import requests,time,collections

requests.packages.urllib3.disable_warnings()

task_id = "logstash_hostlog-f3635f2a48124869bedeea85c5380849"
author_token = "Bearer eea26ce9-fa4c-46ae-8f09-666ec85862b9"

headers = {"Authorization":"%s" %author_token}  #接口验证信息
params = {"index":"%s" %task_id,"rows":10000,"pageSize":1}   #index为任务标识ID，rows为查询多少条数据logstash_applicationlog-32a862d6e5da441c9214abef7ad46372
re = requests.post("https://192.168.50.65/api/applicationLog_es/v1/applicationLog/findAllApplicationLogByPage",headers=headers,verify=False,params=params)


data = re.json() #获取接口返回数据
print(data)
vm_list = data["data"]["data"]   #获取ip数据
count = data["data"]["totalSize"]
print("接口返回总条数：%d，实际总条数:%d"%(count,len(vm_list)))
vm_list_ip = []
vm_list_all = []
#ip去重
if count%10 != 0:
    for_count = count//10+1
else:
    for_count = count//10
for i in range(for_count):
    params = {"index":"%s" %task_id,"rows":10,"pageSize":"%d" %(i*10)}
    # print(params)
    re_value = requests.post("https://192.168.50.65/api/applicationLog_es/v1/applicationLog/findAllApplicationLogByPage",headers=headers,verify=False,params=params)
    data_value = re_value.json()
    vm_list_value = data_value["data"]["data"]
    # time.sleep(1)
    # print("第%d页数据" %i)
    for j in range(1,len(vm_list_value)+1):
        # print("第%d行,ip:%s" %(j,vm_list_value[j-1]["ipAddress"]))
        vm_list_all.append(vm_list_value[j-1]["ipAddress"])
        if vm_list_value[j-1]["ipAddress"] not in vm_list_ip:
            vm_list_ip.append(vm_list_value[j-1]["ipAddress"])
            print("第%d页-第%d行-%s" %(i+1,j,vm_list_value[j-1]["ipAddress"]))
print("共%d台,%s" %(len(vm_list_ip),vm_list_ip))

dic = collections.Counter(vm_list_all)
sum_value = 0
for key in dic:
    print("%s共发送->%d条日志" %(key,dic[key]))
    sum_value = sum_value + dic[key]
print(sum_value)
