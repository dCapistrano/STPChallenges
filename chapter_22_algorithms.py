"""Fizzbuzz"""
def fizz_buzz():
	for i in range(1, 101):
		if i % 3 == 0 and i % 5 == 0:
			print("Fizzbuzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)

fizz_buzz()

"""Sequential Search"""
def ss(number_list, n):
	found = False
	for i in number_list:
		if i == n:
			found = True
			break
	return found

numbers = range(0, 100)
s1 = ss(numbers, 2)
print(s1)
s2 = ss(numbers, 202)
print(s2)

"""Palindrome"""
def palindrome(word):
	word = word.lower()
	return word[::-1] == word

print(palindrome("Mother"))
print(palindrome("mom"))

"""Anagram"""
def anagram(w1, w2):
	w1 = w1.lower()
	w2 = w2.lower()
	return sorted(w1) == sorted(w2)

print(anagram("iceman", "cinema"))
print(anagram("leaf", "tree"))

"""Count Character Occurances"""
def count_characters(string):
	count_dict = {}
	for c in string:
		if c in count_dict:
			count_dict[c] += 1
		else:
			count_dict[c] + 1
	print(count_dict)

count_characters("The Nine Club")






