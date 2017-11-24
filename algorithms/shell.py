class Shell:
    def sort(self, data):
        h = 1
        while h < len(data) / 3:
            h = h * 3 + 1
        while h >= 1:
            for i in range(h, len(data)):
                j = i
                while j >= h and self.less(data[j], data[j - h]):
                    self.exch(data, j, j - h)
                    j -= h
            h //= 3

    def less(self, x, y):
        return x < y

    def exch(self, data, i, min_index):
        data[i], data[min_index] = data[min_index], data[i]


if __name__ == "__main__":
    s = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
    shell = Shell()
    shell.sort(s)
    print(s)
