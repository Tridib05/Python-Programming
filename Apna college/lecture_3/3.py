#Enter names of 3 favorite movies & store in a list:
movies = [input("Movie 1: "), input("Movie 2: "), input("Movie 3: ")]
print("Your movies:", movies)


#Check if a list is a palindrome:
lst = [1, 2, 3, 2, 1]
print(lst == lst.copy()[::-1])


#Count number of students with “A” grade:
grades = ("C", "D", "A", "A", "B", "B", "A")
print("A count =", grades.count("A"))


#Store the same values in a list & sort from “A” to “D”:
grades_list = list(grades)
grades_list.sort()
print("Sorted grades:", grades_list)
