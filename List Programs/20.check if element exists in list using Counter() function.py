from collections import Counter

test_list = [10, 15, 20, 7, 46, 2808]

# Calculating frequencies
frequency = Counter(test_list)

# If the element has frequency greater than 0
# then it exists else it doesn't exist
if(frequency[15] > 0):
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")
