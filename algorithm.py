#import this
import sys

# 1. 已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下

# a = "aAsmr3idd4bgs7Dlsf9eAF"
# b = list(a)
# i = 0
# num = list()
# count = list(a)
# dict_count = dict()

# 1.1 请将a字符串的大写改为小写，小写改为大写。
# 1.2 请将a字符串的数字取出，并输出成一个新的字符串。
# for x in a:
#     if x in string.ascii_lowercase:
#         b[i] = string.ascii_uppercase[string.ascii_lowercase.find(x)]
#         count[i] = string.ascii_uppercase[string.ascii_lowercase.find(x)]
#     elif x in string.ascii_uppercase:
#         b[i] = string.ascii_lowercase[string.ascii_uppercase.find(x)]
#     else:
#         num.append(x)
#         b[i] = x
#     i += 1
# else:
#     print("".join(b))
#     print("".join(num))

# 1.3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
# for y in string.ascii_uppercase:
#     if y in count:
#         dict_count.update({y: count.count(y)})
# else:
#     print(dict_count)

# 1.4 请去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
# y = list()
# z = set()
# for x in b:
#     if b.count(x) == 1:
#         y.append(x)
#     else:
#         z.add(b.index(x))
# t = list(z)
# while i < len(t):
#     y.insert(t[i], a[t[i]])
#     i += 1
# print("".join(y))

# 1.5 请将a字符串反转并输出。例：'abc'的反转是'cba'
# count.reverse()
# print(count)

# 1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
# for x in a:
#     if x not in string.digits:
#         num.append(x)
# else:
#     print(sorted(num, key=str.upper))

# 1.7 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
# x = 'boy'
# total = 0
# while i < len(x):
#     if x[i] in a:
#         total += 1
#     i += 1
# print(total == len(x))

# 1.8 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
# words = ['boy', 'girl', 'bird', 'dirty']
# total = 0
# j = 0
#
# for x in words:
#     for y in x:
#         if y in a:
#             total += 1
#     print(total == len(x))
#     total = 0

# 1.9 输出a字符串出现频率最高的字母
# max_num = 0
# max_num_item = ""
# for x in a:
#     temp = a.count(x)
#     if temp > max_num:
#         max_num = temp
#         max_num_item = x
# print(max_num_item)


# 2.在python命令行里，输入import this 以后出现的文档，统计该文档中，"be" "is" "than" 的出现次数。
# tmp = sys.stdout
# total = 0
# words = ["be", "is", "than"]
# help(this)
# file = open(tmp, 'r')
# for x in words:
#     if x in tmp:
#         total += 1
# file.close()
# print(total)

# 3.一文件的字节数为 102324123499123，请计算该文件按照kb与mb计算得到的大小。
# print(102324123499123 >> 10)
# print(102324123499123 >> 10 >> 10)

# 4.已知  a =  [1,2,3,6,8,9,10,14,17],请将该list转换为字符串，例如 '123689101417'.
# a = [1, 2, 3, 6, 8, 9, 10, 14, 17]
# temp = []
# for x in a:
#     b = str(x)
#     temp.append(b)
# print("".join(temp))