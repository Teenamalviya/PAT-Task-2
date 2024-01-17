'''Write a program to take string and return number of unique character'''
#input= "Guvi Geeks Network Private Limited"

# Taking user input and assign it to variable
yourstring = input("Enter your string : ")

#Creating empty list
a = []

#Looping over user input into order to get character
for i in yourstring:
# Validating whether character is present in the list, if not then adding it to list
    if i not in a:
        a.append(i)
#Printing unique character list and total number of character into it.
print(a)
print(len(a))