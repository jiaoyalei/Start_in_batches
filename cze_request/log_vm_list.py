import requests
requests.packages.urllib3.disable_warnings()
vm_name_list = ["克隆tk-nginx-15.1-wordpress",
                "克隆tk-nginx-15.1-opencart",
                "克隆tk-nginx-15.1-zencart",
                "克隆tk-mysql-15.1-wordpress",
                "克隆tk-mysql-slave-15.1-wordpress",
                "克隆tk-mysql-15.1-phpbb",
                "克隆tk-mysql-slave-15.1-phpbb",
                "克隆tk-mysql-15.1-zencart",
                "克隆tk-mysql-15.1-opencart",
                "ubuntu18.04-server",
                "ubuntu16.04-server",
                "kali-19.1",
                "centos7.5",
                "windows7-64",
                "windows10",
                "windowsserver2019",
                "windowsserver2016",
                "windowsserver2012",
                "win7_克隆_勿删"]
# vm_name_list = ["克隆tk-mysql-15.1-wordpress",
#                 "克隆tk-mysql-slave-15.1-wordpress",
#                 "克隆tk-mysql-15.1-phpbb",
#                 "克隆tk-mysql-slave-15.1-phpbb",
#                 "克隆tk-mysql-15.1-zencart",
#                 "克隆tk-mysql-15.1-opencart"
#
# ]
headers = {"Authorization":"Bearer bfc2e13a-7499-42d8-86bf-f5b50750d742"}
re = requests.post("https://192.168.50.65/api/xplatform/v1/vm/getVmListGroupBase",headers=headers,verify=False)
data = re.json()

vm_list_index = []
for i in range(len(data["data"])):
    if data["data"][i]["name"] in vm_name_list:
        vm_name_value = {}
        vm_name_value["name"] = data["data"][i]["name"]
        vm_name_value["index"] = i+1
        vm_list_index.append(vm_name_value)
print(len(vm_list_index))
print(vm_list_index)
