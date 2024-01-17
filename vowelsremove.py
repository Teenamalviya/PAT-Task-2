'''Write a program that takes a string and returns a new string with all the vowels removed'''

# Enter user string
input_data =input("Enter your string : ")
# Print entered string
print(input_data)

#Remove vowels(a,e,i,o,u) from the string
result = input_data.replace('a','')
result = result.replace('e','')
result = result.replace('i','')
result = result.replace('o','')
result = result.replace('u','')

#Print string without vowels
print(result)