# coding = utf-8
# !/usr/bin/env python
import os
import time


class PinYin(object):

    path = "Files/rawdict_utf16_65105_freq.txt"
    pinyin_list = []
    keyboard_num = ['2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5', '6', '6', '6', '7', '7', '7', '7', '8',
                    '8', '8', '9', '9', '9', '9']
    keyboard_letter = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't','u', 'v', 'w', 'x', 'y', 'z']

    def __init__(self):
        self.pinyin_file = open("pinyin.txt", 'w', encoding='utf-8')
        self.keyboard_file = open("keyboard.txt", 'w', encoding='utf-8')

    def do_file(self):
        print("Starting...")
        start_time = time.time()
        with open(self.path, 'r', encoding='utf-8') as data:
            for x in data:
                self.change_format(x.split(' '))
        self.write_file()
        end_time = time.time()
        return "Write done(%2.2fs). \nPlease check pinyin.txt and keyboard.txt." % (end_time - start_time)

    '''
    eg. change format from "xiexie" to "xie_xie".
    '''
    def change_format(self, data):
        if len(data) == 4:
            self.pinyin_list.append((data[0], "%s" % data[3]))
        elif len(data) == 5:
            self.pinyin_list.append((data[0], "%s_%s" % (data[3], data[4])))
        elif len(data) == 6:
            self.pinyin_list.append((data[0], "%s_%s_%s" % (data[3], data[4], data[5])))
        elif len(data) == 7:
            self.pinyin_list.append((data[0], "%s_%s_%s_%s" % (data[3], data[4], data[5], data[6])))

    def write_file(self):
        length = len(self.pinyin_list)
        str_text = []
        str_key = []
        str_pinyin = ''
        for index in range(length):
            if index < length - 1 and self.pinyin_list[index][1] == self.pinyin_list[index + 1][1]:
                str_text.append(self.pinyin_list[index][0])
            else:
                str_text.append(self.pinyin_list[index][0])
                str_pinyin = self.pinyin_list[index][1]
                self.pinyin_file.write("const unsigned char PY_mb_%s []= {\"%s\"};\n" % (str_pinyin.replace('\n', ''),
                                                                                         "".join(str_text)))
                for num in str_pinyin.replace('\n', '').replace('_', ''):
                    str_key.append(self.keyboard_num[self.keyboard_letter.index(num)])
                self.keyboard_file.write("{0x%s, \"%s\", PY_mb_%s};\n" % ("".join(str_key),
                                                                          str_pinyin.replace('\n', ''),
                                                                          str_pinyin.replace('\n', '')))
                str_text.clear()
                str_key.clear()
        self.pinyin_file.close()
        self.keyboard_file.close()

if __name__ == "__main__":
    manager = PinYin()
    if os.path.exists(manager.path):
        print(manager.do_file())
    else:
        print("The file is not exist, please put the .txt in right directory!")
