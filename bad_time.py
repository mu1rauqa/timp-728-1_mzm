import re


def get_list_time(file):
    with open(file, "r") as file:
        data = file.read()
        list_time = re.findall("(?<=real\s0m)\d\.\d+", data)
        return list(map(float, list_time))


def main():
    list_with_name = ["bad_time_comb.txt", "bad_time_shell.txt", "bad_time_fast.txt", "bad_time_heap.txt"]
    print("============ Сортировка расческой ============")
    print(f"Лучшее время: {min(get_list_time(list_with_name[0]))}")
    print(f"Худшее время: {max(get_list_time(list_with_name[0]))}\n")
    print("============ Сортировка Шелла============")
    print(f"Лучшее время: {min(get_list_time(list_with_name[1]))}")
    print(f"Худшее время: {max(get_list_time(list_with_name[1]))}\n")
    print("============ Быстрая сортировка ============")
    print(f"Лучшее время: {min(get_list_time(list_with_name[2]))}")
    print(f"Худшее время: {max(get_list_time(list_with_name[2]))}\n")
    print("============ Пирамидальная сортировка ============")
    print(f"Лучшее время: {min(get_list_time(list_with_name[3]))}")
    print(f"Худшее время: {max(get_list_time(list_with_name[3]))}\n")


if __name__ == '__main__':
    main()
