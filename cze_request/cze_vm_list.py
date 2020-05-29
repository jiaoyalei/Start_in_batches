import requests

re = requests.post("http://192.168.234.80:18080/nvmp/get_vm_list")
list_value = re.json()
print(list_value)
list_other = []
list_data = []
list_pool = []
for i in range(len(list_value["data"])):
    try:
        if (list_value["data"][i]["pool"]) == "CZE_DERIVE_COURSE":
            list_data.append(list_value["data"][i]["vmid"])
        else:
            list_pool.append(list_value["data"][i]["pool"])
    except Exception:
            list_other.append(list_value["data"][i])
myset = set(list_pool) #myset是另外一个列表，里面的内容是mylist里面的无重复 项
myset_list = list(myset)
stop_list = []
for i in list_data:
    if "5" in str(i)[0:1] or "10" in str(i)[0:2]:
        stop_list.append(i)
text ='''虚机总数：【{vm_num}】
CZE_DERIVE_COURSE分组下【{num0}】条数据、无pool分组共【{num1}】条数据、{group1}分组下【{num2}】条数据、{group2}分组下【{num3}】条数据、{group3}分组下【{num4}】条数据
{del_vm_list}
课程下共【{num5}】台虚机可关闭
{stop_vm_list}
'''.format(vm_num=len(list_value["data"]),num0=len(list_data),
           num1=len(list_other),del_vm_list=list_data,
           group1=myset_list[0],num2=list_pool.count(myset_list[0]),
           group2=myset_list[1],num3=list_pool.count(myset_list[1]),
           group3=myset_list[2],num4=list_pool.count(myset_list[2]),
           num5=len(stop_list),stop_vm_list=stop_list)
print(text)
