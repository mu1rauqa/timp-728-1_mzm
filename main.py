import sys
from random import randint
from fast_sorting import *
from shellsort import *
from comb_sort import *
from heapsort import *
from datetime import datetime
import time


class GenerateList(object):
	def __init__(self, length):
		self.counts = 1000
		self.length = length

	def get_single_list(self, length):  
		return [randint(0, sys.maxsize) for _ in range(self.length)]  # method for generate list

	def gen_lists(self):
		return [self.get_single_list(self.length) for _ in range(self.counts)]  # method for generate lists


def main():
	"""Генерация списков с указанной длиной"""	
	list_length_1 = GenerateList(1).gen_lists()
	list_length_2 = GenerateList(2).gen_lists()
	list_length_3 = GenerateList(3).gen_lists()
	list_length_4 = GenerateList(4).gen_lists()
	list_length_5 = GenerateList(5).gen_lists()
	list_length_10 = GenerateList(10).gen_lists()
	list_length_15 = GenerateList(15).gen_lists()
	list_length_20 = GenerateList(20).gen_lists()
	list_length_25 = GenerateList(25).gen_lists()
	list_length_30 = GenerateList(30).gen_lists()
	list_length_50 = GenerateList(50).gen_lists()
	list_length_75 = GenerateList(75).gen_lists()
	list_length_100 = GenerateList(100).gen_lists()
	list_length_250 = GenerateList(250).gen_lists()
	list_length_500 = GenerateList(500).gen_lists()

	"""Сортировка расческой"""
	comb_srt = CombSort(list_length_500[0])
	print(comb_srt)
	combo_result = comb_srt.get_result()
	print(f"Список: {combo_result[0]}\nКол-во операций: {combo_result[1]}\nВремя: {combo_result[2]}")

	"""Сортировка Шелла"""
	shell_srt = ShellSort(list_length_10[0])
	print(shell_srt)
	shell_result = shell_srt.get_result()
	print(f"Список: {shell_result[0]}\nКол-во операций: {shell_result[1]}")

	"""Быстрая сортировка"""
	print("============ Быстрая сортировка ============")
	fast_srt = get_fast_sort(list_length_10[0])
	print(f"Список: {fast_srt[0]}\n Кол-во операций: {fast_srt[1]}")

	"""Пирамидальная сортировка"""
	print("============ Пирамидальная сортировка ============")
	heap_srt = HeapSort(list_length_10[0])
	heap_result = heap_srt.get_result()
	print(f"Список: {heap_result[0]}\n Кол-во операций: {heap_result[1]}")


if __name__ == '__main__':
	main()