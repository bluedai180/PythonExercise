from openpyxl import Workbook
from openpyxl.styles import Border, Side, Font, Alignment, NamedStyle


f = open("E:\worktest\python\PythonExercise\Files\\releasenotes.APV749.txt", 'r', encoding='utf-8')
wb = Workbook()
ws = wb.active
ws.title = "svn_info"
ws.append(['Bug ID', '责任人', '问题描述', '原因分析', '修改方案', 'svn 版本'])

i = 0
lines = []
info = []
for data in f:
    i += 1
    lines.append(data)
    if data.startswith("-------"):
        info.append("".join(lines).replace("------------------------------------------------------------------------",
                                           ""))
        lines.clear()

info_total = [x for x in info if x != '\n']
f.close()
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
            temp.append("null")
        if "原因分析" in text:
            temp.append("".join(text_list[b + 1:c]).lstrip())
        else:
            temp.append("null")
        if "修改方案" in text:
            temp.append("".join(text_list[c + 1:d]).lstrip())
        else:
            temp.append("null")
        temp.append(svn_id)
        ws.append(temp)
        temp.clear()
    except ValueError:
        print("以下信息格式不正确：")
        print(text_list)
    except IndexError:
        print("以下信息格式不正确：")
        print(text_list)

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

ws.column_dimensions['A'].width = 15
ws.column_dimensions['B'].width = 15
ws.column_dimensions['C'].width = 80
ws.column_dimensions['D'].width = 55
ws.column_dimensions['E'].width = 55
ws.column_dimensions['F'].width = 10
for i in range(ws.max_row):
    ws.row_dimensions[i + 1].height = 30
for x in ws[1]:
    x.style = title
for x in ws['A'][1:]:
    x.style = content
for x in ws['B'][1:]:
    x.style = content
for x in ws['C'][1:]:
    x.style = content_long
for x in ws['D'][1:]:
    x.style = content_long
for x in ws['E'][1:]:
    x.style = content_long
for x in ws['F'][1:]:
    x.style = content




wb.save("E:\worktest\python\PythonExercise\Files\svn_info.xlsx")


text = info_total[16]
text_list = text.split('\n')
print(text_list)

author = text_list[2].split(']')[0].split(":")[1]
bug_id = text_list[2].split(']')[1].split("+")[1]
svn_id = text_list[0].split('|')[0].replace('r', '')

temp.append(bug_id)
temp.append(author)

# try:
#     a = text_list.index("1.问题描述")
#     b = text_list.index("2.原因分析")
#     c = text_list.index("3.修改方案")
#     d = text_list.index("4.影响范围")
#     if "问题描述" in text:
#         print(text_list[a + 1:b])
#         temp.append("".join(text_list[a + 1:b]))
#     else:
#         print("null")
#     if "原因分析" in text:
#         print(text_list[b + 1:c])
#         temp.append("".join(text_list[b + 1:c]))
#     else:
#         print("null")
#     if "修改方案" in text:
#         print(text_list[c + 1:d])
#         temp.append("".join(text_list[c + 1:d]))
#     else:
#         print("null")
#     temp.append(svn_id)
# except ValueError:
#     print("以下信息格式不正确：")
#     print(text_list)


# a = text_list.index("1.问题描述")
# b = text_list.index("2.原因分析")
# c = text_list.index("3.修改方案")
# d = text_list.index("4.影响范围")
# if "问题描述" in text:
#     print(text_list[a + 1:b])
#     temp.append("".join(text_list[a + 1:b]))
# else:
#     print("null")
# if "原因分析" in text:
#     print(text_list[b + 1:c])
#     temp.append("".join(text_list[b + 1:c]))
# else:
#     print("null")
# if "修改方案" in text:
#     print(text_list[c + 1:d])
#     temp.append("".join(text_list[c + 1:d]))
# else:
#     print("null")
# temp.append(svn_id)
# print(temp)


