from openpyxl import load_workbook, Workbook
from openpyxl.styles import Border, Side, Font, Alignment, NamedStyle
import os

path = "E:\worktest\python\PythonExercise\Files\events_log_20170217_180212.log"
excel_path = "E:\worktest\python\PythonExercise\Files\log.xlsx"

info_total = []

if os.path.exists(excel_path):
    os.remove(excel_path)

with open(path, 'r', encoding='utf-8') as data:
    for x in data:
        if "am_crash" in x:
            info = []
            # time = ''.join(x[0:18])
            name = ''.join(x[43:]).split(',')[2]
            exception = ''.join(x[43:]).split(',')[4]
            java_name = ' '.join(''.join(x[43:]).split(',')[-2:]).replace(']', '')
            # info.append(time)
            info.append(name)
            info.append(exception)
            info.append(java_name)
            info_total.append(info)

info_total.sort(key=lambda x: x[0])

num = []
for x in info_total:
    num.append(info_total.count(x))

temp_name = []
for x in info_total:
    temp_name.append(x[0])

temp_num = []
for x in temp_name:
    temp_num.append(temp_name.count(x))

for i in range(len(temp_num)):
    info_total[i].insert(0, temp_num[i])

total_num = []

info_final = []

for i in range(len(num)):
    info_total[i].append(num[i])

for x in info_total:
    if x not in info_final:
        info_final.append(x)

line_num = []

for i in range(len(info_final)):
    if i < len(info_final) - 1:
        if info_final[i][1] != info_final[i + 1][1]:
            line_num.append(i + 2)
    else:
        line_num.append(len(info_final) + 1)

print(line_num)

wb = Workbook()
ws = wb.active
ws.title = "events_log"
ws.append(['总数', '进程名', '错误类型', '错误位置', '复现次数'])

ws.column_dimensions['A'].width = 10
ws.column_dimensions['B'].width = 40
ws.column_dimensions['C'].width = 40
ws.column_dimensions['D'].width = 40
ws.column_dimensions['E'].width = 10

if len(line_num) == 1:
    ws.merge_cells('A%s:A%s' % (2, line_num[-1]))
    ws.merge_cells('B%s:B%s' % (2, line_num[-1]))

for i in range(len(line_num)):
    if i < len(line_num) - 1:
        if line_num[i + 1] - line_num[i] != 1:
            ws.merge_cells('A%s:A%s' % (line_num[i] + 1, line_num[i + 1]))
            ws.merge_cells('B%s:B%s' % (line_num[i] + 1, line_num[i + 1]))

for x in info_final:
    ws.append(x)
    print(x)

wb.save(excel_path)
