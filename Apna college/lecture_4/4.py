#Store word meanings in a dictionary:
dictionary = {
  "table": ["a piece of furniture", "list of facts & figures"],
  "cat": "a small animal"
}
print(dictionary)


#Count how many classrooms (unique subjects) are needed:
subjects = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]
print("Classrooms needed:", len(set(subjects)))


#Enter marks of 3 subjects from user & store in dictionary:
marks = {}
marks["Math"] = int(input("Math marks: "))
marks["English"] = int(input("English marks: "))
marks["Science"] = int(input("Science marks: "))
print(marks)


#Store 9 and 9.0 as separate values in a set:
s = {9, "9.0"}
print(s)