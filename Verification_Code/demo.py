import datetime

str_p = '2019-01-30 15:29:08'
dateTime_p = datetime.datetime.strptime(str_p,'%Y-%m-%d %H:%M:%S')
print(type(dateTime_p)) # 2019-01-30 15:29:08