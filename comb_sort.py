import sys
from main import *


class CombSort(object):
    def __init__(self, lst):
        self._count = 0
        self._lst = lst

    def __str__(self):
        return "============ Сортировка расчёской ============"

    def comb_sort(self):
        step = len(self._lst)
        swapped = True
        while step > 1 or swapped:
            step = max(1, int((step * 10) / 13))
            swapped = False
            for i in range(len(self._lst) - step):
                self._count += 1
                if self._lst[i] > self._lst[i + step]:
                    self._lst[i], self._lst[i + step] = self._lst[i + step], self._lst[i]
                    swapped = True

    def get_result(self):
        self.comb_sort()
        return [self._lst, self._count]


def main():
    for length in list(map(int, sys.argv[1:])):  # цикл для всех
        tmp_count = 0
        for current_list in GenerateList(length).gen_lists():  # цикл для получения одного из тысячи списков
            tmp_obj = CombSort(current_list)
            tmp_count += tmp_obj.get_result()[1]
        print(f"Длина списка: {length} \tКоличество операций: {tmp_count}")


if __name__ == '__main__':
    main()
