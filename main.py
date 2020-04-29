import sys
from random import randint


class GenerateList(object):
	def __init__(self, length):
		self.counts = 1000
		self.length = length

	def get_single_list(self, length):
		return [randint(0, sys.maxsize) for _ in range(self.length)]  # method for generate list

	def gen_lists(self):
		return [self.get_single_list(self.length) for _ in range(self.counts)]  # method for generate lists


def main():
	pass


if __name__ == '__main__':
	main()
