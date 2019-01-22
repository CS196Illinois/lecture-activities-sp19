

"""This method should print 'hello world' to the screen. There is no return value for this method."""
def hello_world():
	pass


"""
Given a list of integers, find the maximum element.
	Input: A list of integers
	Output: The maximum value in the list
"""
def find_max(my_list):
	return 0


'''
Given a list of integers, determine the maximum number less n.
	Input: [1,4,2,14, 11], n = 6
	Output: 4
	Hint: You may wish to use your find_max function in this function
'''
def find_max_less_than(my_list, n):
	return 0




"""
Determine if all characters in the string are unique. Meaning no character occurs more than once.
	Input: A string
	Output: 
		True if it is unique
		False if the string is not unique
"""
def is_unique(str_in):
	pass


"""
Determine the character that occurs most frequently in  the input string
	Input: A string
	Output:
		The character that occurs most frequently
"""
def most_common_char(str_in):
	pass


"""
Determine if n is prime.
	Input: An integer n
	Output:
		True: if n is prime
		False: if n is not prime
"""
def is_prime(n):
	pass


'''
Given a string, print out the letters that are capitalized.
Input: 'HellO World'
We should print out the letters 'H', 'O', and 'W'
Hint: the lower() and upper() functions may be userful
'''
def find_capitals(str_in):
	pass

"""
Given a series of words separated by spaces, split the statement up into a list where each element is a word.
	Input:
		'hello World how is it going'
	Output:
		['hello', 'World', 'how', 'is', 'it', 'going']
	Hint: Look up the split() function
"""
def make_list(str_in):
	pass



if __name__ == '__main__':
	print("Welcome to the Basics Lecture")
	hello_world()

	list_a = [1,5,43,5,12,155,123]
	if find_max(list_a) == 155:
		print("You found the correct max value for the first list")

	list_b = [i % 123 for i in range(100000)]
	if find_max(list_b) == max(list_b):
		print("You found the correct max value for the second list")

	if(find_max_less_than(list_b, 125) == 122):
		print("your find_max_less_than function found the correct value than less n")


	#Try writing your own tests for the rest of the problem!


