

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
    test_arr = [3301, 1984, 256, 13]
    print(get_fast_sort(test_arr))


if __name__ == '__main__':
    main()