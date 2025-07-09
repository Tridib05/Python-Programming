#Create a file practice.txt and write data into it:
data = '''Hi everyone
we are learning File I/O
using Java.
I like propgranmming in Java.'''
with open("practice.txt", "w") as file:
    file.write(data)


#WAF to replace all occurrences of “Java” with “Python”:
def replace_java_with_python():
    with open("practice.txt", "r") as file:
        content = file.read()
    content = content.replace("Java", "Python")
    with open("practice.txt", "w") as file:
        file.write(content)
replace_java_with_python()


#Search if the word “learning” exists in the file or not:
with open("practice.txt", "r") as file:
    content = file.read()
if "learning" in content:
    print("The word 'learning' exists in the file.")
else:
    print("The word 'learning' does NOT exist in the file.")


#WAF to find in which line the word “learning” occurs first:
def find_learning_line(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    for i, line in enumerate(lines, start=1):
        if "learning" in line:
            return i
    return -1
print(find_learning_line("practice.txt"))


#WAF to count even numbers from a file where numbers are separated by commas:
#Assume file content like:12, 45, 78, 91, 34, 55
def count_even_numbers(filename):
    with open(filename, "r") as file:
        content = file.read()
    numbers = [int(x.strip()) for x in content.split(",")]
    even_count = sum(1 for n in numbers if n % 2 == 0)
    print("Even numbers count:", even_count)
count_even_numbers("numbers.txt")

