from bigO import *
import unittest

class tester_fibonacci(unittest.TestCase):
	def test_basic(self):
		n= 10
		self.assertEquals(fibonacci(n), 55)

	def test_big(self):
		n = 100
		self.assertEquals(fibonacci(n), 354224848179261915075)

class tester_freqs(unittest.TestCase):
	def test_basic(self):
		array = range(10)
		answer = dict(zip(range(10), [1]*10))
		self.assertEquals(count_freqs(array), answer)

	def test_big(self):
		array = range(1000000)
		two_list = array + range(1000000)
		answer = dict(zip(array, [2]*1000000))
		self.assertEquals(count_freqs(array), answer)


class tester_three_sum(unittest.TestCase):
	def test_basic(self):
		array = [1,2,3]
		self.assertEquals(three_sum(array, 6), True)
		self.assertEquals(three_sum(array, 7), False)



	def test_big(self):
		array = [(1000000 - i) for i in range(-1, 1000000)]
		self.assertEquals(three_sum(array, 1000001), True)
		self.assertEquals(three_sum(array, 10000000), False)

class tester_closest(unittest.TestCase):
	def test_basic(self):
		array = [5,14, 3, 77]
		self.assertEquals(find_closest(array), 2)

	def test_big(self):
		array = [(100000 - i)**2 for i in range(99998)]
		array = [10] + array
		self.assertEquals(find_closest(array), 1)

class tester_pairs(unittest.TestCase):
	def test_basic(self):
		A = [9,14]
		B = [5,11,16]
		self.assertEquals(count_greater_pairs(A, B), 3)

	def test_big(self):
		B = range(1000000)
		A = [-2] + [(i+23434324343) for i in range(10000)]
		self.assertEquals(count_greater_pairs(A, B), len(B))
		A = [-3,-2, 2]
		self.assertEquals(count_greater_pairs(A, B), 2*len(B) + (len(B) - 3))


if __name__ == "__main__":
	unittest.main(module=__name__, buffer=True, exit=False)