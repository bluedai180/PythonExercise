# 1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。

# def func(*num):
#     result = list(num)
#     return sorted(result)[0], sorted(result)[len(result) - 1]

# 2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。

# def func(*string):
#     result_list = []
#     result_list = [(x, len(x)) for x in list(string)]
#     return sorted(result_list, key=lambda y: y[1], reverse=True)[0][0]
# print(func('aaa', 'b', 'vvvvvvvv'))

# 3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
# import time
#
#
# def get_doc(module):
#     help(module)
# print(get_doc(time))

# 例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。

# 4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。

# def get_text(f):
#     file = open(f, 'r')
#     for x in file.readlines():
#         return x
# print(get_text(''))


# 5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
# import glob
# def get_dir(folder):
#     return glob.glob(folder)
# print(get_dir("/home/blue/python"))

# 1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。
def get_num(num):
    if isinstance(num, list):
        for x in num:
            if isinstance(x, int) is False:
                return "the num is not int"
        return list(filter(lambda y: y % 2 == 0, num))
    else:
        return "the num is not list"
assert get_num([2, 1, 30]) == [2, 30]

# 2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。

import urllib
#def get_page(url):


# 3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。

# def func(*num_list):
#     for x in num_list:
#         if isinstance(x, list) is False:
#             return "the num_list is not list"
#     return sorted(num_list, key=lambda y: len(y), reverse=True)[0]
# print(func([1, 2], [1, 2, 3]))

# 4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。

# def get_dir(f):

