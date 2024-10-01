# First character in each word is
# uppercase and remaining lowercase
s = 'Geeks For Geeks'
print(s.istitle())

# First character in first
# word is lowercase
s = 'geeks For Geeks'
print(s.istitle())

# Third word has uppercase
# characters at middle
s = 'Geeks For GEEKs'
print(s.istitle())
# Ignore the digit 6041, hence returns True
s = '6041 Is My Number'
print(s.istitle())

# word has uppercase
# characters at middle
s = 'GEEKS'
print(s.istitle())
