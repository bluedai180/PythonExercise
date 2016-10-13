#coding = utf-8
import time

result = []
# data = open("twitter.txt", 'r', encoding='utf-8')

# 1.该文本里，有多少个用户。（要求：输出为一个整数。）
# for x in data.readlines():
#     result.append(x.split(',')[1].replace('\"', ""))
# print(len(result))
# print(len(set(result)))

# 2.该文本里，每一个用户的名字。 （要求：输出为一个list。）
# for x in data.readlines():
#     result.append(x.split(',')[6].replace('\"', ""))
# print(list(set(result)))

# print(data.readline().split(',')[6].replace('\"', ''))

# 3.该文本里，有多少个2012年11月发布的tweets。
# for x in data.readlines():
#     print(x)
#     if time.strptime(x.split(',')[6].replace('\"', ""), '%Y-%m-%d %H:%M:%S').tm_year == '12':
#         result.append(x.split(',')[6])
#
# print(result)
# data.close()

# with open("twitter.txt", 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line)