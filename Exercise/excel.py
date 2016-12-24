import os

from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment
import datetime
import sys

'''
文档：https://openpyxl.readthedocs.io/en/default/
功能：整理组内日报脚本
作者：bluedai180
时间：2016/12/23
'''


class Daily(object):
    name = []
    file_path = '../Files/excel_files'
    file_name = '../Files/excel_files/应用一课日报.xlsx'
    excel_title = '应用一课日报'
    excel_file = []
    left, right, top, bottom = [Side(style='thin', color='000000')] * 4
    border = Border(left=left, right=right, top=top, bottom=bottom)

    def __init__(self):
        self.wb_new = Workbook()
        self.ws_new = self.wb_new.active
        self.ws_new.title = self.excel_title

    def check_file(self):
        self.excel_file = os.listdir(self.file_path)
        excel_name = []
        for x in self.excel_file:
            excel_name.append(x.split('_')[1][0:-5])
        for x in self.name:
            if x not in excel_name:
                print(x)

    def do_files(self, commend):
        self.ws_new.append(['项目', '工作类别', 'Bug ID', '简要描述', '优先级', '是否reopen', 'reopen原因', '解决方案',
                            '原因', '责任人', '日期', '备注'])
        for x in self.excel_file:
            print("正在读取: %s" % x)
            wb = load_workbook('%s/%s' % (self.file_path, x))
            ws = wb.get_sheet_by_name(commend)
            excel_cell = list(ws.rows)
            temp = []
            for x in excel_cell[1:]:
                for y in x:
                    if type(y.value) is datetime.datetime:
                        temp.append(y.value.strftime("%Y/%m/%d"))
                    else:
                        temp.append(y.value)
                self.ws_new.append(temp)
                temp.clear()

        self.format_file()
        self.wb_new.save(self.file_name)


    def format_file(self):
        #self.ws_new.column_dimensions.width = 70
        self.ws_new.dimensions.SheetFormatProperties(defaultColWidth=50, defaultRowHeight=50)
        cell_new = list(self.ws_new.rows)
        for x in cell_new:
            for y in x:
                y.border = self.border





if __name__ == '__main__':
    daily = Daily()
    print("以下人员未交日报：\n")
    daily.check_file()
    is_do = input("\n是否继续生成日报？[y/n]:")
    if is_do == 'y':
        commend = input("\n需要输出星期几的日报：")
        daily.do_files(commend)
        print("\n请查看生成的日报。")
        # daily.format_file()
    elif is_do == 'n':
        sys.exit(0)
    else:
        print("请输入y或者n！")



















