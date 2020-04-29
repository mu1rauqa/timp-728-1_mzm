

class HeapSort(object):
    def __init__(self, lst):
        self._lst = lst
        self._count = 0

    def __str__(self):
        return "Пирамидальная сортировка"

    def heapify(self):
        start = (len(self._lst) - 2) // 2
        while start >= 0:
            self._count += 1
            self.sift_down(start, len(self._lst) - 1)
            start -= 1

    def sift_down(self, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and self._lst[child] < self._lst[child + 1]:
                self._count += 1
                child += 1
            if child <= end and self._lst[root] < self._lst[child]:
                self._count += 1
                self._lst[root], self._lst[child] = self._lst[child], self._lst[root]
                root = child
            else:
                return

    def run(self):
        self.heapify()
        end = len(self._lst) - 1
        while end > 0:
            self._lst[end], self._lst[0] = self._lst[0], self._lst[end]
            self._count += 1
            self.sift_down(0, end - 1)
            self._count += 1
            end -= 1

    def get_result(self):
        self.run()
        return [self._lst, self._count]


def main():
    test_lst = [1, 2, 3]
    obj = HeapSort(test_lst)
    print(obj.get_result())


if __name__ == '__main__':
    main()