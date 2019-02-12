import unittest
from week5 import *


class tester_replace_char(unittest.TestCase):

	def test_simple(self):
		str_in = 'abc'
		c1 = 'b'
		c2 = 'd'
		self.assertEqual(replace_char(str_in, c1, c2), 'adc')

	def test_more(self):
		str_in = 'abceefcgefefd'
		c1 = 'e'
		c2 = ' '
		self.assertEqual(replace_char(str_in, c1, c2), 'abc  fcg f fd')

	def test_case(self):
		str_in = 'Abcabc'
		c1 = 'a'
		c2 = 'f'
		self.assertEqual(replace_char(str_in, c1, c2), 'fbcfbc')


class tester_increment_string(unittest.TestCase):
	def test_basic(self):
		self.assertEqual(increment_string('aBc'), 'bCd')
		self.assertEqual(increment_string('aaa'), 'bbb')

	def test_with_z(self):
		self.assertEqual(increment_string('abcZz'), 'bcdAa')

	def test_empty(self):
		self.assertEqual(increment_string(''), '')

class tester_remove_duplicate(unittest.TestCase):
	def test_no_dups(self):
		my_list = [i for i in range(30)]
		self.assertEqual(remove_duplicates(my_list), my_list)
	
	def test_all_dups(self):
		a = ['a']*30
		self.assertEqual(remove_dulicates(a), ['a'])

	def test_basic(self):
		my_list = [0, 1,2,3,4,5,5,5,6,7,8,8,8,9]
		self.assertEqual(remove_dulicates(my_list), range(10))

	def test_keep_order(self):
		my_list = [i for i in range(10, -1, -1)]
		test_list = my_list.append(10)
		self.assertEqual(remove_dulicates(test_list), my_list)

class tester_overlap(unittest.TestCase):
	def test_small(self):
		a = [1,2,3,4]
		b = [3,4]
		self.assertEqual(overlap(a, b), [3,4])

	def test_no_overlap(self):
		a = [1,2,3,4,5,6]
		b = [7,8,9]
		self.assertEqual(overlap(a, b), [])

	def test_with_duplicates(self):
		a = [1,2,3,4,5,5,6,7]
		b = [-10, 5, 5, 7,7, 8]
		self.assertEqual(overlap(a,b), [5,7])

	def test_large(self):
		a = [(i*3) for i in range(100)]
		b = [(i*2) for i in range(30)]
		self.assertEqual(overlap(a,b), [(i*6) for i in range(10)])

class tester_mystery(unittest.TestCase):
	def test_simple(self):
		my_arr = ['5', '1', '3', '2']
		retval = mystery_func(int, sorted, my_arr)
		self.assertEqual(retval, [1,2,3,5])

	def test_more(self):
		x = lambda a : -a
		my_arr = range(30)
		retval = mystery_func(x, max, my_arr)
		self.assertEqual(retval, 0)


	def test_extra(self):
		double = lambda a : 2*a
		my_arr = range(30)
		retval = mystery_func(double, sum, my_arr)
		self.assertEqual(retval, sum(my_arr)*2)


class tester_replace_str(unittest.TestCase):
	def test_basic(self):
		str_in = 'Hello World'
		str1 = 'hello'
		str2 = 'world'
		self.assertEqual(replace_str(str_in, str1, str2), 'world World')

	def test_more(self):
		str_in = 'wow what a great job'
		str1 = 'JOB'
		str2 = ''
		self.assertEqual(replace_str(str_in, str1, str2), 'wow what a great ')
	def test_no_replace(self):
		str_in = 'hello world'
		str1 = 'wow'
		str2 = 'hello world'
		self.assertEqual(replace_str(str_in, str1, str2), str_in)


if __name__ == "__main__":
	unittest.main(module=__name__, buffer=True, exit=False)
