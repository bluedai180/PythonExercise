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
    x_list = list(x)
    for i in range(len(x_list)):
        if i < len(x_list) - 1:
            if x_list[i] != x_list[i + 1]:
                temp = [y for y, v in enumerate(num) if v == x_list[i]]
                if x_list.count(x_list[i]) == len(temp):
                    index.extend([str(x) for x in temp])
                else:
                    index.append(str(temp[0]))
            else:
                pass
        else:
            pass
    print(index)

    # if "".join(index) == "".join(sorted("".join(index))):
    #     print(x)
    #     print(len(x))
        # exit()
    index.clear()




