#coding = utf-8
import time

result = []
data = open("twitter.txt", 'r', encoding='utf-8')

# 1.该文本里，有多少个用户。（要求：输出为一个整数。）
# for x in data.readlines():
#     result.append(x.split(',')[1])
# print(len(result))
# print(len(set(result)))

# 2.该文本里，每一个用户的名字。 （要求：输出为一个list。）
# for x in data.readlines():
#     result.append(x.split(',')[2])
# print(list(set(result)))

# 3.该文本里，有多少个2012年11月发布的tweets。


data.close()