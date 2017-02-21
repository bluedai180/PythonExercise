from openpyxl import Workbook
from openpyxl.styles import Border, Side, Font, Alignment, NamedStyle
import os

class MonkeyLog(object):

    log_path = "/home/blue/python/AlgorithmPython/Files/25179；25187/monkeysys.log"
    excel_path = "/home/blue/python/AlgorithmPython/Files/log.xlsx"

    info_total = []
    info_final = []

    def __init__(self):
        if os.path.exists(self.excel_path):
            os.remove(self.excel_path)

    def get_info(self):
        name = []
        detail = []
        with open(self.log_path, 'r', encoding='utf-8') as data:
            for x in data:
                if x.startswith('// CRASH: '):
                    name.append(x.split(' ')[2])
                if x.startswith('// Long Msg:'):
                    detail.append(' '.join(x.split(' ')[3:]).replace('\n', ''))
        if len(name) != len(detail):
            print("Wrong message !!!!!!!")

        for i in range(len(name)):
            temp = [name[i], detail[i]]
            self.info_total.append(temp)

    def analyze_info(self):
        self.info_total.sort(key=lambda x: x[0])
        each_bug_num = self.count_bug(self.info_total)
        each_app_num = self.count_app(self.info_total)
        for i in range(len(each_app_num)):
            self.info_total[i].insert(0, each_app_num[i])
        for i in range(len(each_bug_num)):
            self.info_total[i].append(each_bug_num[i])
        for x in self.info_total:
            if x not in self.info_final:
                self.info_final.append(x)

    def write_excel(self):
        wb = Workbook()
        ws = wb.active
        ws.title = "monkey_log"
        ws.append(['总数', '进程名', '错误信息', '复现次数'])

        merge_line_num = self.count_merge(self.info_final)
        length = len(merge_line_num)
        for i in range(length):
            if length == 1:
                ws.merge_cells('A%s:A%s' % (2, merge_line_num[-1]))
                ws.merge_cells('B%s:B%s' % (2, merge_line_num[-1]))
            elif i < length - 1:
                if merge_line_num[i + 1] - merge_line_num[i] != 1:
                    ws.merge_cells('A%s:A%s' % (merge_line_num[i] + 1, merge_line_num[i + 1]))
                    ws.merge_cells('B%s:B%s' % (merge_line_num[i] + 1, merge_line_num[i + 1]))

        for x in self.info_final:
            ws.append(x)
        self.format_excel(ws)
        wb.save(self.excel_path)

    def count_app(self, info):
        temp_name = []
        temp_num = []
        for x in info:
            temp_name.append(x[0])
        for x in temp_name:
            temp_num.append(temp_name.count(x))
        return temp_num

    def count_bug(self, info):
        temp_num = []
        for x in info:
            temp_num.append(self.info_total.count(x))
        return temp_num

    def count_merge(self, info):
        temp_num = []
        length = len(info)
        for i in range(length):
            if i < length - 1:
                if info[i][1] != info[i + 1][1]:
                    temp_num.append(i + 2)
            else:
                temp_num.append(length + 1)
        return temp_num

    def format_excel(self, ws):
        ws.column_dimensions['A'].width = 8
        ws.column_dimensions['B'].width = 30
        ws.column_dimensions['C'].width = 100
        ws.column_dimensions['D'].width = 10
        for i in range(ws.max_row):
            ws.row_dimensions[i + 1].height = 30
        left, right, top, bottom = [Side(style='thin', color='000000')] * 4
        title = NamedStyle(name="title")
        title.font = Font(name=u'宋体', size=11)
        title.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        title.border = Border(left=left, right=right, top=top, bottom=bottom)
        content = NamedStyle(name="content")
        content.font = Font(name=u'宋体', size=11)
        content.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        content.border = Border(left=left, right=right, top=top, bottom=bottom)
        content_long = NamedStyle(name="content_long")
        content_long.font = Font(name=u'宋体', size=11)
        content_long.border = Border(left=left, right=right, top=top, bottom=bottom)
        content_long.alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
        for x in ws[1]:
            x.style = title
        for x in ws['A:B']:
            for y in x:
                y.style = content
        for x in ws['C'][1:]:
            x.style = content_long
        for x in ws['D'][1:]:
            x.style = content

if __name__ == '__main__':
    log = MonkeyLog()
    log.get_info()
    log.analyze_info()
    log.write_excel()
