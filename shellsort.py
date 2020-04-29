import sys
from main import *


class ShellSort(object):
    def __init__(self, lst):
        self._count = 0
        self.lst = lst

    def __str__(self):
        return "============ Сортировка Шелла ============"

    def shell_sort(self):
        step = len(self.lst) // 2  # шаг
        while step > 0:
            for i in range(step, len(self.lst)):
                self._count += 1
                tmp = self.lst[i]
                j = i
                while j >= step and self.lst[j - step] > tmp:
                    self._count += 1
                    self.lst[j] = self.lst[j - step]
                    j = j - step
                self.lst[j] = tmp
            step //= 2
        return self.lst

    def get_result(self):
        self.shell_sort()
        return [self.lst, self._count]


def main():
    for length in list(map(int, sys.argv[1:])):  # цикл для всех
        tmp_count = 0
        for current_list in GenerateList(length).gen_lists():  # цикл для получения одного из тысячи списков
            tmp_obj = ShellSort(current_list)
            tmp_count += tmp_obj.get_result()[1]
        print(f"Длина списка: {length} \tКоличество операций: {tmp_count}")


if __name__ == '__main__':
    main()
