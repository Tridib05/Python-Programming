# Initializing list
test_list = [10, 15, 20, 7, 46, 2808]

print("Checking if 15 exists in list")
x=list(map(str,test_list))
y="-".join(x)

if y.find("15") !=-1:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")
