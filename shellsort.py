

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
    lst = [3, 1, 2]
    obj = ShellSort(lst)
    print(obj.get_result())


if __name__ == '__main__':
    main()