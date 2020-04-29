from main import *
import sys


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
    for length in list(map(int, sys.argv[1:])):  # цикл для всех
        tmp_count = 0
        for current_list in GenerateList(length).gen_lists():  # цикл для получения одного из тысячи списков
            tmp_obj = HeapSort(current_list)
            tmp_count += tmp_obj.get_result()[1]
        print(f"Длина списка: {length} \tКоличество операций: {tmp_count}")


if __name__ == '__main__':
    main()
