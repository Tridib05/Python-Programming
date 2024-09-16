# Function to find the largest element in the list
def FindLargest(itr, ele, list1):

  # Base condition
    if itr == len(list1):
        print("Largest element in the list is: ", ele)
        return

      # Check max condition
    if ele < list1[itr]:
        ele = list1[itr]

        # Recursive solution
    FindLargest(itr+1, ele, list1)

    return

  # input list
list1 = [2, 1, 7, 9, 5, 4]

FindLargest(0, list1[0], list1)
