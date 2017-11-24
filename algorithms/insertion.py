class Insertion:
    def sort(self, data):
        for i in range(1, len(data)):
            index = i
            while self.less(data[index], data[index - 1]) and index > 0:
                self.exch(data, index, index - 1)
                index -= 1

    def less(self, x, y):
        return x < y

    def exch(self, data, i, min_index):
        data[i], data[min_index] = data[min_index], data[i]


if __name__ == "__main__":
    s = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
    insertion = Insertion()
    insertion.sort(s)
    print(s)
