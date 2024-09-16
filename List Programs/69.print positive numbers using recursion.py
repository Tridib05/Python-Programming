#Function to print even numbers in a list
def PrintEven(itr,list1):
  if itr == len(list1): #Base Condition
    return 
  if list1[itr]>=0:
    print(list1[itr],end = " ")
  PrintEven(itr+1,list1)  #Recursive Function Call
  return

list1 = [-5,7,-19,10,9] #list of numbers
PrintEven(0,list1) #Function Call 

#This code is contributed by vinay pinjala
