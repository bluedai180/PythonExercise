class Bubble:
    def sort(self, data):
        temp = len(data) - 1
        for i in range(len(data)):
            last_index = temp
            for j in range(last_index):
                if not self.less(data[j], data[j + 1]):
                    self.exch(data, j, j + 1)
                    temp = j
            if last_index == temp:
                break

    def less(self, x, y):
        return x < y

    def exch(self, data, i, min_index):
        data[i], data[min_index] = data[min_index], data[i]


if __name__ == "__main__":
    s = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
    bubble = Bubble()
    bubble.sort(s)
    print(s)
