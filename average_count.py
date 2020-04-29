import re
import numpy as np
import matplotlib.pyplot as plt
from math import log, pow


def get_average_counts(file):
    with open(file, "r") as file:
        data = file.read()
        list_counts = re.findall("Количество операций: (!?\d+)", data)
        return sum(map(int, list_counts))


def get_counts(file):
    with open(file, "r") as file:
        data = file.read()
        list_counts = re.findall("Количество операций: (!?\d+)", data)
        return list(map(int, list_counts))


def get_time(file):
    with open(file, "r") as file:
        data = file.read()
        list_time = re.findall("(?<=real\s0m)\d\.\d+", data)
        return list(map(float, list_time))


def get_average_time(file):
    with open(file, "r") as file:
        data = file.read()
        list_time = re.findall("(?<=real\s0m)\d\.\d+", data)
        return sum(map(float, list_time))


def draw_graph():
    names_files_count = ["combsort_count.txt", "shell_count.txt", "fast_count.txt", "heap_count.txt"]
    names_files_time = ["combsort_time.txt", "shell_time.txt", "fast_time.txt", "heap_time.txt"]
    list_length = np.array([1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 50, 75, 100, 250, 500])

    # """Graph for comb on counts"""
    # list_counts = np.array(get_counts(names_files_count[0]))
    # y1 = list_length
    # y2 = (list_length * np.log2(list_length))
    # y3 = list_length ** 2
    # y4 = list_length ** 3
    # y5 = np.log2(list_length)
    #
    # fig = plt.figure(figsize=(0.2, 2.5), facecolor="#f1f1f1")
    # left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    # ax = fig.add_axes((left, bottom, width, height))
    # ax.set_title("Сортировка расческой")
    # ax.set_xlabel("n")
    # ax.set_ylabel("C(n)")
    # ax.set_xlim(0, 500)
    # ax.set_ylim(0, 700)
    # ax.plot(list_length, list_counts, color="red", label="C(n)")
    # ax.plot(list_length, y1, color="green", label="y=x")
    # ax.plot(list_length, y2, 'g', color="blue", label="y=x * log(x)")
    # ax.plot(list_length, y3, 'g', color="pink", label="y=x^2")
    # ax.plot(list_length, y4, 'g', color="black", label="y=x^3")
    # ax.legend()
    # plt.show()
    #
    # """Graph for comb on time"""
    # list_counts = np.array(get_time(names_files_time[0]))
    # y1 = list_length
    # y2 = (list_length * np.log2(list_length))
    # y3 = list_length ** 2
    # y4 = list_length ** 3
    #
    # fig = plt.figure(figsize=(0.2, 2.5), facecolor="#f1f1f1")
    # left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    # ax = fig.add_axes((left, bottom, width, height))
    # ax.set_title("Сортировка расческой ")
    # ax.set_xlabel("n")
    # ax.set_ylabel("T(n)")
    # ax.set_xlim(0, 500)
    # ax.set_ylim(0, 700)
    # ax.plot(list_length, list_counts, color="red", label="T(n)")
    # ax.plot(list_length, y1, color="green", label="y=x")
    # ax.plot(list_length, y2, 'g', color="blue", label="y=x * log(x)")
    # ax.plot(list_length, y3, 'g', color="pink", label="y=x^2")
    # ax.plot(list_length, y4, 'g', color="black", label="y=x^3")
    # ax.legend()
    # plt.show()
    #
    # """Graph for shell on counts"""
    # list_counts = np.array(get_counts(names_files_count[1]))
    # y1 = list_length
    # y2 = (list_length * np.log2(list_length))
    # y3 = list_length ** 2
    # y4 = list_length ** 3
    # y5 = np.log2(list_length)
    #
    # fig = plt.figure(figsize=(0.2, 2.5), facecolor="#f1f1f1")
    # left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    # ax = fig.add_axes((left, bottom, width, height))
    # ax.set_title("Сортировка Шелла")
    # ax.set_xlabel("n")
    # ax.set_ylabel("C(n)")
    # ax.set_xlim(0, 500)
    # ax.set_ylim(0, 700)
    # ax.plot(list_length, list_counts, color="red", label="C(n)")
    # ax.plot(list_length, y1, color="green", label="y=x")
    # ax.plot(list_length, y2, 'g', color="blue", label="y=x * log(x)")
    # ax.plot(list_length, y3, 'g', color="pink", label="y=x^2")
    # ax.plot(list_length, y4, 'g', color="black", label="y=x^3")
    # ax.legend()
    # plt.show()
    #
    # """Graph for shell on time"""
    # list_counts = np.array(get_time(names_files_time[1]))
    # y1 = list_length
    # y2 = (list_length * np.log2(list_length))
    # y3 = list_length ** 2
    # y4 = list_length ** 3
    #
    # fig = plt.figure(figsize=(0.2, 2.5), facecolor="#f1f1f1")
    # left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    # ax = fig.add_axes((left, bottom, width, height))
    # ax.set_title("Сортировка Шелла ")
    # ax.set_xlabel("n")
    # ax.set_ylabel("T(n)")
    # ax.set_xlim(0, 500)
    # ax.set_ylim(0, 700)
    # ax.plot(list_length, list_counts, color="red", label="T(n)")
    # ax.plot(list_length, y1, color="green", label="y=x")
    # ax.plot(list_length, y2, 'g', color="blue", label="y=x * log(x)")
    # ax.plot(list_length, y3, 'g', color="pink", label="y=x^2")
    # ax.plot(list_length, y4, 'g', color="black", label="y=x^3")
    # ax.legend()
    # plt.show()

    """Graph for fast on counts"""
    list_counts = np.array(get_counts(names_files_count[2]))
    y1 = list_length
    y2 = (list_length * np.log2(list_length))
    y3 = list_length ** 2
    y4 = list_length ** 3
    y5 = np.log2(list_length)

    fig = plt.figure(figsize=(0.2, 2.5), facecolor="#f1f1f1")
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax = fig.add_axes((left, bottom, width, height))
    ax.set_title("Быстрая сортировка")
    ax.set_xlabel("n")
    ax.set_ylabel("C(n)")
    ax.set_xlim(0, 500)
    ax.set_ylim(0, 10000000)
    ax.plot(list_length, list_counts, color="red", label="C(n)")
    ax.plot(list_length, y1, color="green", label="y=x")
    ax.plot(list_length, y2, 'g', color="blue", label="y=x * log(x)")
    ax.plot(list_length, y3, 'g', color="pink", label="y=x^2")
    ax.plot(list_length, y4, 'g', color="black", label="y=x^3")
    ax.legend()
    plt.show()

    """Graph for fast on time"""
    list_counts = np.array(get_time(names_files_time[2]))
    y1 = list_length
    y2 = (list_length * np.log2(list_length))
    y3 = list_length ** 2
    y4 = list_length ** 3

    fig = plt.figure(figsize=(0.2, 2.5), facecolor="#f1f1f1")
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax = fig.add_axes((left, bottom, width, height))
    ax.set_title("Быстрая сортировка")
    ax.set_xlabel("n")
    ax.set_ylabel("T(n)")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.plot(list_length, list_counts, color="red", label="T(n)")
    ax.plot(list_length, y1, color="green", label="y=x")
    ax.plot(list_length, y2, 'g', color="blue", label="y=x * log(x)")
    ax.plot(list_length, y3, 'g', color="pink", label="y=x^2")
    ax.plot(list_length, y4, 'g', color="black", label="y=x^3")
    ax.legend()
    plt.show()

    # """Graph for heap on counts"""
    # list_counts = np.array(get_counts(names_files_count[3]))
    # y1 = list_length
    # y2 = (list_length * np.log2(list_length))
    # y3 = list_length ** 2
    # y4 = list_length ** 3
    # y5 = np.log2(list_length)
    #
    # fig = plt.figure(figsize=(0.2, 2.5), facecolor="#f1f1f1")
    # left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    # ax = fig.add_axes((left, bottom, width, height))
    # ax.set_title("Пирамидальная сортировка")
    # ax.set_xlabel("n")
    # ax.set_ylabel("C(n)")
    # ax.set_xlim(0, 500)
    # ax.set_ylim(0, 700)
    # ax.plot(list_length, list_counts, color="red", label="C(n)")
    # ax.plot(list_length, y1, color="green", label="y=x")
    # ax.plot(list_length, y2, 'g', color="blue", label="y=x * log(x)")
    # ax.plot(list_length, y3, 'g', color="pink", label="y=x^2")
    # ax.plot(list_length, y4, 'g', color="black", label="y=x^3")
    # ax.legend()
    # plt.show()
    #
    # """Graph for heap on time"""
    # list_counts = np.array(get_time(names_files_time[3]))
    # y1 = list_length
    # y2 = (list_length * np.log2(list_length))
    # y3 = list_length ** 2
    # y4 = list_length ** 3
    #
    # fig = plt.figure(figsize=(0.2, 2.5), facecolor="#f1f1f1")
    # left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    # ax = fig.add_axes((left, bottom, width, height))
    # ax.set_title("Пирамидальная сортировка")
    # ax.set_xlabel("n")
    # ax.set_ylabel("T(n)")
    # ax.set_xlim(0, 500)
    # ax.set_ylim(0, 700)
    # ax.plot(list_length, list_counts, color="red", label="T(n)")
    # ax.plot(list_length, y1, color="green", label="y=x")
    # ax.plot(list_length, y2, 'g', color="blue", label="y=x * log(x)")
    # ax.plot(list_length, y3, 'g', color="pink", label="y=x^2")
    # ax.plot(list_length, y4, 'g', color="black", label="y=x^3")
    # ax.legend()
    # plt.show()


def main():
    names_files_count = ["combsort_count.txt", "shell_count.txt", "fast_count.txt", "heap_count.txt"]
    names_files_time = ["combsort_time.txt", "shell_time.txt", "fast_time.txt", "heap_time.txt"]
    """Average counts for every algorithm."""
    print(f"Average counts for comb: {get_average_counts(names_files_count[0]) // 15 + 1}\n")
    print(f"Average counts for shell: {get_average_counts(names_files_count[1]) // 15 + 1}\n")
    print(f"Average counts for fast: {get_average_counts(names_files_count[2]) // 15 + 1}\n")
    print(f"Average counts for heap: {get_average_counts(names_files_count[3]) // 15 + 1}\n")

    """Average time for every algorithm."""
    print(f"Average time for comb: {get_average_time(names_files_time[0]) / 15.0}\n")
    print(f"Average time for shell: {get_average_time(names_files_time[1]) / 15.0}\n")
    print(f"Average time for fast: {get_average_time(names_files_time[2]) / 15.0}\n")
    print(f"Average time for heap: {get_average_time(names_files_time[3]) / 15.0}\n")

    draw_graph()


if __name__ == '__main__':
    main()
