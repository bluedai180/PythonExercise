from openpyxl import load_workbook
from openpyxl import Workbook

'''
https://openpyxl.readthedocs.io/en/default/
'''
# wb = load_workbook("../Files/test.xlsx")
# table = wb.get_sheet_by_name('Sheet1')
#
# rows = table.max_row
# cols = table.max_column
# print(tuple(table.rows))
# print(list(table.columns))

wb = Workbook()
ws = wb.active
ws.title = "New Title"
ws['A1'] = 42
ws.append([1, 2, 3])
import datetime
ws['A2'] = datetime.datetime.now()
ws.cell(row=4, column=2, value=10)
col_range = ws['A1:C2']
print(list(col_range))

wb.save("sample.xlsx")

