import os
import os.path
import xml.dom.minidom
from openpyxl import Workbook
from openpyxl.styles import Border, Side, Font, Alignment, NamedStyle

rootdir = "/data/YL50B71/android/packages/apps"
# values_dir_name = ["values", "values-in", "values-bd", "values-np", "values-id", "values-vn", "values-my", "values-de", "values-fr", "values-ru", "values-cz", "values-sk", "values-hr", "values-gr", "values-rs", "values-lt", "values-pl", "values-es", "values-it", "values-lv", "values-ee", "values-nl", "values-pt", "values-fi", "values-dk", "values-se", "values-si", "values-il", "values-hu", "values-ua", "values-bg", "values-ro", "values-mk", "values-no", "values-tr", "values-ar"]
values_dir_name = ["values", "values-in", "values-bd", "values-np", "values-id", "values-vn", "values-my", "values-de"]
values_dir_path = []
# values_file_path = ["/data/YL50B71/android/packages/apps/SnapdragonCamera/res/values/strings.xml"]
values_file_path = []
keys_en = []
values_en = []
path_en = []

keys_other = []
values_other = []


info_en = []
info_in = []
info_bd = []
info_np = []
info_id = []
info_vn = []
info_my = []
info_de = []
info_fr = []
info_ru = []
info_cz = []
info_sk = []
info_hr = []
info_gr = []
info_rs = []
info_lt = []
info_pl = []
info_es = []
info_it = []
info_lv = []

info_other = [info_en, info_in, info_bd, info_np, info_id, info_vn, info_my, info_de]
#info_ee ", "values-nl", "values-pt", "values-fi", "values-dk", "values-se", "values-si", "values-il", "values-hu", "values-ua", "values-bg", "values-ro", "values-mk", "values-no", "values-tr", "values-ar"

wb = Workbook()
ws = wb.active
ws.title = "svn_info"
ws.append(["路径", "key", "values", "values-in"])

for parent,dirnames,filenames in os.walk(rootdir):
    for x in values_dir_name:
        if x in dirnames:
            values_dir_path.append(os.path.join(parent, x))

for x in values_dir_path:
    for y in os.listdir(x):
        values_file_path.append("%s/%s" % (x, y))

for x in values_file_path:
    xmldoc = xml.dom.minidom.parse(x)
    code = xmldoc.getElementsByTagName('string')
    for node in code:
        for item in node.childNodes:
            value_tag = x.split("/")[-2]
            if value_tag == "values":
                try:
                    info_en.append((node.getAttribute('name'), item.data))
                    keys_en.append(node.getAttribute('name'))
                    path_en.append(x)
                    values_en.append(item.data)
                except AttributeError as e:
                    print(x)
                    print(node.getAttribute('name'))
                    pass
            else:
                for dir_name in values_dir_name[1:]:
                    if value_tag == dir_name:
                        try:
                            info_other[values_dir_name.index(dir_name)].append((node.getAttribute('name'), item.data))
                        except AttributeError as e:
                            print(x)
                            print(node.getAttribute('name'))
                            pass
                    else:
                        pass

info_total = []
info_total_temp = []
info_temp = []

temp_keys = [z[0] for z in info_other[1]]

for x in keys_en:
    info_total_temp.append(path_en[keys_en.index(x)])
    info_total_temp.append(x)
    info_total_temp.append(values_en[keys_en.index(x)])
    if x not in [z[0] for z in info_other[1]]:
        info_total_temp.append('')
    else:
        info_total_temp.append(info_other[1][temp_keys.index(x)][1])
    info_total.append(info_total_temp)
    print(info_total_temp)
    ws.append(info_total_temp)
    info_total_temp.clear()

    # if x not in temp_keys:
    #     info_total_temp.append('')
    # else:
    #     info_total_temp.append(info_other[1][temp_keys.index(x)][1])
    # info_total.append(info_total_temp)
    # ws.append(info_total_temp)
    # info_total_temp.clear()

wb.save("test.xlsx")

