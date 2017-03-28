import os
from openpyxl import Workbook
from openpyxl.styles import Border, Side, Font, Alignment, NamedStyle
import tkinter.filedialog as filedialog
from tkinter import *

class ReleaseNotes(object):
    path = ""

    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active

    def get_each_info(self):
        lines = []
        info = []
        file = open(self.path, 'r', encoding='utf-8')
        for data in file:
            lines.append(data)
            if data.startswith("-------"):
                info.append(
                    "".join(lines).replace("------------------------------------------------------------------------",
                                           ""))
                lines.clear()
        info_total = [x for x in info if x != '\n']
        file.close()
        self.get_detail_info(info_total)

    def get_detail_info(self, info_total):
        temp = []
        for text in info_total:
            text_list = text.split('\n')
            try:
                author = text_list[2].split(']')[0].split(":")[1].lstrip()
                bug_id = text_list[2].split(']')[1].split("+")[1].lstrip()
                svn_id = text_list[0].split('|')[0].replace('r', '').lstrip()
                temp.append(bug_id)
                temp.append(author)
                a = text_list.index("1.问题描述")
                b = text_list.index("2.原因分析")
                c = text_list.index("3.修改方案")
                d = text_list.index("4.影响范围")
                if "问题描述" in text:
                    temp.append("".join(text_list[a + 1:b]).lstrip())
                else:
                    temp.append("")
                if "原因分析" in text:
                    temp.append("".join(text_list[b + 1:c]).lstrip())
                else:
                    temp.append("")
                if "修改方案" in text:
                    temp.append("".join(text_list[c + 1:d]).lstrip())
                else:
                    temp.append("")
                temp.append(svn_id)
                self.ws.append(temp)
                temp.clear()
            except ValueError:
                print(text_list)
            except IndexError:
                print(text_list)

    def write_excel(self):
        self.ws.title = "svn_info"
        self.ws.append(['Bug ID', '责任人', '问题描述', '原因分析', '修改方案', 'svn 版本'])
        left, right, top, bottom = [Side(style='thin', color='000000')] * 4
        title = NamedStyle(name="title")
        title.font = Font(name=u'宋体', size=11, bold=True)
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
        self.ws.column_dimensions['A'].width = 15
        self.ws.column_dimensions['B'].width = 15
        self.ws.column_dimensions['C'].width = 80
        self.ws.column_dimensions['D'].width = 55
        self.ws.column_dimensions['E'].width = 55
        self.ws.column_dimensions['F'].width = 10
        for i in range(self.ws.max_row):
            self.ws.row_dimensions[i + 1].height = 30
        for x in self.ws[1]:
            x.style = title
        for x in self.ws['A'][1:]:
            x.style = content
        for x in self.ws['B'][1:]:
            x.style = content
        for x in self.ws['C'][1:]:
            x.style = content_long
        for x in self.ws['D'][1:]:
            x.style = content_long
        for x in self.ws['E'][1:]:
            x.style = content_long
        for x in self.ws['F'][1:]:
            x.style = content

        self.wb.save(os.path.dirname(os.path.abspath(self.path)) + "/" + os.path.basename(self.path).replace(".txt", ".xlsx"))

    @staticmethod
    def open_win():
        root = Tk()
        root.title("svn release notes 分析")
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = ws / 2 - 400 / 2
        y = hs / 2 - 200 / 2
        root.geometry("400x200+%d+%d" % (x, y))

        def callback():
            ReleaseNotes.path = filedialog.askopenfilename()
            entry.insert(0, ReleaseNotes.path)

        button = Button(root, text="选择ReleaseNotes文件", command=callback)
        quit_btn = Button(root, text="确定", command=root.destroy)
        entry = Entry(root)
        entry.pack(side=TOP, anchor="nw", fill=X, pady=40)
        button.pack(side=TOP)
        quit_btn.pack(side=TOP, pady=10)
        root.mainloop()

if __name__ == "__main__":
    ReleaseNotes.open_win()
    notes = ReleaseNotes()
    notes.get_each_info()
    notes.write_excel()
