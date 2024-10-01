#using bulit in function
str = "geeks"
print(len(str))

#using for loop
def findLen(str):
	counter = 0
	for i in str:
		counter += 1
	return counter
str = "geeks"
print(findLen(str))

#using while loop
def findLen(str):
	counter = 0
	while str[counter:]:
		counter += 1
	return counter

str = "geeks"
print(findLen(str))

#using join and count method
def findLen(str):
	if not str:
		return 0
	else:
		some_random_str = 'py'
		return ((some_random_str).join(str)).count(some_random_str) + 1
str = "geeks"
print(findLen(str))

#using reduce method
import functools
def findLen(string):
	return functools.reduce(lambda x,y: x+1, string, 0)
string = 'geeks'
print(findLen(string))



