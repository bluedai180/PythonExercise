# coding = utf-8
import time

result = []
data = open("Files/twitter.txt", 'r', encoding='utf-8')


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
# result_dict = dict()
# for x in data.readlines():
#     result.append((x.split('","')[6].split(" ")[0], x.split('","')[2]))
# result_day = [(x, result.count(x)) for x in set(result)]
# result_day.sort(key=lambda k: (k[0][0], k[1]))
# for y in result_day:
#     result_dict[y[0][0]] = y[0][1]
# print(result_dict)
# data.close()

# 7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets）
# for x in data.readlines():
#     if x.split('","')[6].split(" ")[0] == "2012-11-03":
#         result.append(time.strptime(x.split('","')[6], '%Y-%m-%d %H:%M:%S').tm_hour)
# result_hour = [(y, result.count(y)) for y in result]
# print(set(result_hour))
# data.close()

# 8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）
# for x in data.readlines():
#     result.append(x.split('","')[7])
# result_source = [(y, result.count(y)) for y in result]
# print(set(result_source))
# data.close()

# 9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)
# for x in data.readlines():
#     if "https://twitter.com/umiushi_no_uta" in x.split('","')[34]:
#         result.append(x.split('","')[34])
# print(len(result))
# data.close()

# 10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）
# for x in data.readlines():
#     if x.split('","')[1] == "573638104":
#         result.append(x.split('","')[1])
# print(len(result))
# data.close()

# 11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。
# result_list = []
# def read_file():
#     for x in data.readlines():
#         result.append(x.split('","')[1])
#     data.close()
#
#
# def get_most_uid(*uids):
#     for y in uids:
#         if y in result:
#             result_list.append((y, result.count(y)))
#         else:
#             return
#
#     return sorted(result_list, key=lambda x: x[1], reverse=True)[0][0]
#
# read_file()
# search = ["573638104", "86044459"]
# print(get_most_uid(*search))

# 12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）
# for x in data.readlines():
#     result.append((x.split('","')[1], len(x.split('","')[4])))
# data.close()
#
# print(sorted(result, key=lambda y: y[1], reverse=True)[0][0])

# 13. 该文本里，谁转发的URL最多 （要求：输出用户的uid，字符串格式。）
# for x in data.readlines():
#     if x.split('","')[34] != "":
#         result.append(x.split('","')[1])
# data.close()
# result_list = list(set([(y, result.count(y)) for y in result]))
# print(sorted(result_list, key=lambda y : y[1], reverse=True)[0][0])

# 14. 该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）
# for x in data.readlines():
#     if time.strptime(x.split('","')[6], '%Y-%m-%d %H:%M:%S').tm_hour == 11:
#         result.append(x.split('","')[2])
#
# result_list = list(set([(y, result.count(y)) for y in result]))
# print(sorted(result_list, key=lambda z: z[1], reverse=True)[0][0])
# data.close()

# 15. 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）
# for x in data.readlines():
#     if x.split('","')[33] != "":
#         result.append(x.split('","')[1])
# result_list = list(set([(y, result.count(y)) for y in result]))
# print(sorted(result_list, key=lambda z: z[1], reverse=True)[0][0])
print(list(map(lambda x: x > 1, [1, 2, 3])))