import requests

def cze_stop_vm(vmid):
    count = 0
    stop_list = []
    url = "http://192.168.234.80:18080/nvmp"  #http://192.168.234.80:18080/nvmp/stop/
    re = requests.post("%s/get_vm_list_by_tpl/%d"%(url,vmid))
    list_value = re.json()
    print("当前关闭虚机vmid：%d下派生所有虚机,共%d台" %(vmid,len(list_value['data'])))
    new_list = []
    for i in list_value['data']:
        if i[0:1] not in ("4","5"):
            new_list.append(i)
            re = requests.post(r"%s/stop/%s" %(url,i))
            value = re.json()
            try:
                print("正在关闭虚机{%s},"%i,value["msg"])
            except Exception as e:
                print("正在关闭虚机{%s},"%i,value["data"])
                stop_list.append(i)
                count +=1
    print("实际关机%d台,关机列表：%s"%(count,stop_list))
if __name__ == "__main__":
    '''
    性能测试课程001-vmid：479
    选修课BurpSuite-vmid：128023000
    '''
    vmid = [3199,128023000] #,128023000
    for i in vmid:
        cze_stop_vm(i)
