import itertools

num = [1, 4, 2, 3, 5]
length = len(num)
index = []
num_sort = sorted(num)

for i in range(length):
    num_total = list(itertools.combinations(num_sort, length - i))
    for x in num_total:
        for y in list(x):
            index.append(str(num.index(y)))
        if "".join(index) == "".join(sorted("".join(index))):
            print(x)
            print(len(x))
            exit()
        index.clear()




