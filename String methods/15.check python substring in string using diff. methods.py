#using index method
any_string = "Geeks for Geeks substring "
start = 0
end = 1000
print(any_string.index('substring', start, end))

#using list comprehension
s="geeks for geeks" 
s2="geeks" 
print(["yes" if s2 in s else "no"])

#using lambda function
s="geeks for geeks" 
s2="geeks" 
x=list(filter(lambda x: (s2 in s),s.split())) 
print(["yes" if x else "no"])

#using slicing
def is_substring(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return True
    return False
string = "A geeks in need is a geek indeed"
substring = "geeks"
print(is_substring(string,substring))

