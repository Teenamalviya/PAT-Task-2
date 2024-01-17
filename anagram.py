# Assign input strings to the variables
input_data1 =input("Enter first string : ")
input_data2 =input("Enter second string : ")
#Create two empty list
lis1 = []
lis2 = []
# Iterate over the first and second strings
for data1 in input_data1:
    lis1.append(data1)
for data2 in input_data2:
    lis2.append(data2)
# Sort both the list
lis1.sort()
lis2.sort()
# Compare both the list
if (lis1 == lis2):
    print("Both String are Anagram: True")
else:
    print("Both Strings are Anagram: False")