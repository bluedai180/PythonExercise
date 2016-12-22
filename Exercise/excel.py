import os

from openpyxl import load_workbook
from openpyxl import Workbook

'''
https://openpyxl.readthedocs.io/en/default/
北京应用一课日报--xxx
'''
# wb = load_workbook("../Files/test1.xlsx")
# table = wb.get_sheet_by_name('Sheet1')
#
# rows = table.max_row
# cols = table.max_column
# print(tuple(table.rows))
# print(list(table.columns))

# wb = Workbook()
# ws = wb.active
# ws.title = "New Title"
# ws['A1'] = 42
# ws.append([1, 2, 3])
# import datetime
# ws['A2'] = datetime.datetime.now()
# ws.cell(row=4, column=2, value=10)
# col_range = ws['A1:C2']
# print(list(col_range))
#
# wb.save("sample.xlsx")


name = ['姜怀修', '李硕', '耿文达', '吴镇宇', '周影星', '贾勇强', '崔京浩']
excel_file = os.listdir('../Files/excel_files')
excel_name = []
excel_info = []
for x in excel_file:
    excel_name.append(x.split('_')[1][0:-5])

for x in name:
    if x not in excel_name:
        print(x)

wb_new = Workbook()
ws_new = wb_new.active
ws_new.title = "应用一课日报"


for x in excel_file:
    wb = load_workbook('../Files/excel_files/%s' % x)
    ws = wb.get_sheet_by_name('星期一')
    excel_cell = list(ws.rows)
    temp = []
    for x in excel_cell[1:]:
        for y in x:
            temp.append(y.value)
        ws_new.append(temp)
        temp.clear()

wb_new.save("应用一颗日报.xlsx")


















