

"""This method should print 'hello world' to the screen. There is no return value for this method."""
def hello_world():
	print("hello world")


"""
Given a list of integers, find the maximum element.
	Input: A list of integers
	Output: The maximum value in the list
"""
def find_max(my_list):
	max_value = my_list[0]
	for element in my_list:
		if element > max_value:
			max_value = element
	return max_value



'''
Given a list of integers, determine the maximum number less n.
	Input: [1,4,2,14, 11], n = 6
	Output: 4
	Hint: You may wish to use your find_max function in this function
'''
def find_max_less_than(my_list, n):
	new_list = []
	for elem in my_list:
		if elem < n:
			new_list.append(elem)
	return find_max(new_list)

"""
Determine if all characters in the string are unique. Meaning no character occurs more than once.
	Input: A string
	Output: 
		True if it is unique
		False if the string is not unique
"""
def is_unique(str_in):
	letters = {}
	for let in str_in:
		if let in letters:
			return False
		letters[let] = 1
	return True


"""
Determine the character that occurs most frequently in  the input string
	Input: A string
	Output:
		The character that occurs most frequently
"""
def most_common_char(str_in):
	letters = {}
	for let in str_in:
		if let in letters:
			letters[let] += 1
		else:
			letters[let] = 1
	max_character = str_in[0]
	max_char_times = letters[str_in[0]]
	for let in letters:
		if letters[let] > max_char_times:
			max_character = let
			max_char_times = letters[let]
	return max_character
	


"""
Determine if n is prime.
	Input: An integer n
	Output:
		True: if n is prime
		False: if n is not prime
"""
def is_prime(n):
	if n == 1 or n == 2:
		return True
	for i in range(2,n):
		if n % i == 0:
			return False
	return True


'''
Given a string, print out the letters that are capitalized.
Input: 'HellO World'
We should print out the letters 'H', 'O', and 'W'
Hint: the lower() and upper() functions may be userful
'''
def find_capitals(str_in):
	for let in str_in:
		if let == let.upper():
			print(let)

"""
Given a series of words separated by spaces, split the statement up into a list where each element is a word.
	Input:
		'hello World how is it going'
	Output:
		['hello', 'World', 'how', 'is', 'it', 'going']
	Hint: Look up the split() function
"""
def make_list(str_in):
	return str_in.split(' ')



if __name__ == '__main__':
	hello_world()

	list_a = [1,5,43,5,12,155,123]
	if find_max(list_a) == 155:
		print("You found the correct max value for the first list")

	list_b = [i % 123 for i in range(100000)]
	if find_max(list_b) == max(list_b):
		print("You found the correct max value for the second list")

	if(find_max_less_than(list_b, 125) == 122):
		print("your find_max_less_than function found the correct value than less n")

	if(is_unique('abcd') and not is_unique('ababab')):
		print('Is_unique works')
	if(most_common_char('abacabc') == 'a'):
		print('find max char works!')
	if is_prime(12) and not is_prime(23452):
		print('is prime works!')
	if make_list('hello world') == ['hello', 'world']:
		print('make list works!')
	print('according to your find capitals functions. The capital letters in \'heLLo\' are')
	find_capitals('heLLo')


