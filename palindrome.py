# Enter user input and assign it to variable
inputstring = input("Enter your string : ")
inputstring = inputstring.upper()
# Assign empty string to the variable
w = ""
#Looping over input string to get characters and adding to the string inorder to create reverse string
for x in inputstring:
    w = x+w
#Comparing both input and reverse string
if inputstring == w:
    print("The given string is a palindrome")
else:
    print("The string is not a palindrome")