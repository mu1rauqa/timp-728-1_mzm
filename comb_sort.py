import cProfile
import datetime


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
        start_time = datetime.datetime.now()
        self.comb_sort()
        end_time = datetime.datetime.now()
        result_time = start_time - end_time
        return [self._lst, self._count, result_time.microseconds]


def main():
    test_lst = [3, 2, 1]
    obj = CombSort(test_lst)


if __name__ == '__main__':
    cProfile.run('main()')
