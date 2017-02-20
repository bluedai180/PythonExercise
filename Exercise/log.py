from openpyxl import load_workbook, Workbook
from openpyxl.styles import Border, Side, Font, Alignment, NamedStyle

path = "/home/blue/python/AlgorithmPython/Files/music/hipadlog/logs/adb/events_log_20160830_211152.log"
excel_path = "/home/blue/python/AlgorithmPython/Files/adb.xlsx"
# 时间，进程名，错误类型，复现次数

info_total = []

with open(path, 'r') as data:
    for x in data:
        if "am_crash" in x:
            info = []
            # time = ''.join(x[0:18])
            name = ''.join(x[43:]).split(',')[2]
            exception = ''.join(x[43:]).split(',')[4]
            java_name = ''.join(x[43:]).split(',')[-2:]
            # info.append(time)
            info.append(name)
            info.append(exception)
            info.append(java_name)
            info_total.append(info)

num = []
i = 0
for x in info_total:
    num.append(info_total.count(x))

info_final = []

for i in range(len(num)):
    info_total[i].append(num[i])

for x in info_total:
    if x not in info_final:
        info_final.append(x)

wb = Workbook()
ws = wb.active
ws.title = "events_log"
ws.append(['进程名', '错误类型', '复现次数'])

for x in info_final:
    x.pop(2)
    ws.append(x)

ws.column_dimensions['A'].width = 20
ws.column_dimensions['B'].width = 20
ws.column_dimensions['C'].width = 20

wb.save(excel_path)
print(info_final)
