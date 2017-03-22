import itertools

num = [9, 5, 8, 4, 9, 4, 10]
num_dict = {'0': 9, '1': 5, '2': 8, '3': 4, '4': 9, '5': 4, '6': 10}
length = len(num)
index = []
num_sort = sorted(num)
# print([i for i,v in enumerate(num) if v == 5])
# print(num[1:].index(9))

# for i in range(length):
#     num_total = list(itertools.combinations(num_sort, length - i))
#     for x in num_total:
#         for y in list(x):
#             if ()
#             index.append(str(num.index(y)))
#         if "".join(index) == "".join(sorted("".join(index))):
#             print(x)
#             print(len(x))
#             exit()
#         index.clear()

num_total = list(itertools.combinations(num_sort, 4))
for x in num_total:
    print(x)
    for y in list(x):
        temp = [i for i, v in enumerate(num) if v == y]
        if (len(temp) > 1):
            # for z in temp:
            #     index.append(str(z))
            pass
        else:
            index.append(str(temp[0]))

    if "".join(index) == "".join(sorted("".join(index))):
        print(x)
        print(len(x))
        exit()
    index.clear()




