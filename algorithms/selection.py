class Selection:
    def sort(self, data):
        for i in range(len(data)):
            min_index = i
            for j in range(i + 1, len(data)):
                if self.less(data[min_index], data[j]):
                    min_index = j
            self.exch(data, i, min_index)

    def less(self, x, y):
        return x > y

    def exch(self, data, i, min_index):
        data[i], data[min_index] = data[min_index], data[i]


if __name__ == "__main__":
    selection = Selection()
    s = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
    selection.sort(s)
    print(s)
