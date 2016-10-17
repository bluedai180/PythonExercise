#coding = utf-8
import time

result = []
data = open("twitter.txt", 'r', encoding='utf-8')

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
#     if time.strptime(x.split('","')[6], '%Y-%m-%d %H:%M:%S').tm_year == 2012 and \
#                     time.strptime(x.split('","')[6], '%Y-%m-%d %H:%M:%S').tm_mon == 11:
#         result.append(x.split(',')[6])
# print(len(result))
# data.close()

# 4.该文本里，有哪几天的数据？
# for x in data.readlines():
#     result.append(x.split('","')[6])
# print(sorted(set(result)))
# data.close()

# 5.该文本里，在哪个小时发布的数据最多？
# for x in data.readlines():
#     result.append(time.strptime(x.split('","')[6], '%Y-%m-%d %H:%M:%S').tm_hour)
# result_hours = [(x, result.count(x)) for x in set(result)]
# print(sorted(result_hours, key=lambda k : k[1], reverse=True)[0][0])
# data.close()

# 6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）
for x in data.readlines():
    result.append((x.split('","')[6].split(" ")[0], x.split('","')[1]))
print(dict(result))
data.close()