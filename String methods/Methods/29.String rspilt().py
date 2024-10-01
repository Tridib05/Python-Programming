# splits the string at index 12
# i.e.: the last occurrence of g
word = 'geeks, for, geeks'
print(word.rsplit('g', 1))

# Splitting at '@' with maximum splitting
# as 1
word = 'geeks@for@geeks'
print(word.rsplit('@', 1))
