import sys

sys.setrecursionlimit(1000000)


class Merge:
    def merge_sort(self, lists):
        if len(lists) <= 1:
            return lists
        num = len(lists) // 2
        left = self.merge_sort(lists[:num])
        right = self.merge_sort(lists[num:])
        return self.merge(left, right)

    def merge(self, left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result


if __name__ == "__main__":
    s = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
    merge = Merge()
    print(merge.merge_sort(s))
