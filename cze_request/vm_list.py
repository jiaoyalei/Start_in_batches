import requests,json
import xlwt
reponse = requests.post("http://192.168.235.143:18080/nvmp/get_vm_list")
data_value = reponse.content
print(data_value)
json_data = json.dumps(data_value)
print(json_data)
#
# print(data_value["data"][3]["pool"])