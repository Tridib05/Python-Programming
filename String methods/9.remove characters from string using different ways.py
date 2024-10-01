#using string.translate()
str = 'Geeks123For123Geeks'
print(str.translate({ord(i): None for i in '123'}))

#using slice
test_str = "GeeksForGeeks"
new_str = test_str[:2] + test_str[3:]
print ("The string after removal of i'th character : " + new_str)

#using str.join()
test_str = "GeeksForGeeks"
new_str = ''.join([test_str[i] for i in range(len(test_str)) if i != 2])
print ("The string after removal of i'th character : " + new_str)

#using bytearray
def remove_char(s, i):
	b = bytearray(s, 'utf-8')
	del b[i]
	return b.decode()
s = "hello world"
i = 4
s = remove_char(s, i)
print(s)

#using removeprefix()
s="GeeksforGeeks"
s1=s.removeprefix("G")
s2=s[:5]+s[5:].removeprefix("f")
print(s1)
print(s2)

