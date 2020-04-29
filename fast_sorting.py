import sys
from main import *


count = 0
def fast_sort(lst):
    global count
    count += 1
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]  # опорная точка
        min_arr = [i for i in lst[1:] if i < pivot]  # список с элементами меньше опорного элем.
        max_arr = [i for i in lst[1:] if i >= pivot]  # список с элементами больше опорного элем.
        return fast_sort(min_arr) + [pivot] + fast_sort(max_arr)


def get_fast_sort(lst):
    return [fast_sort(lst), count]


def main():
    for length in list(map(int, sys.argv[1:])):  # цикл для всех
        tmp_count = 0
        average_count = 0
        for current_list in GenerateList(length).gen_lists():  # цикл для получения одного из тысячи списков
            tmp_obj = get_fast_sort(current_list)
            tmp_count += tmp_obj[1]
        print(f"Длина списка: {length} \tКоличество операций: {tmp_count}")


if __name__ == '__main__':
    main()
