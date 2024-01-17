# Enter the user string and assign to variable
input_data = input("Enter your string : ")
# Create empty dictionary
frequency = {}
# Looping over the user input string
for s in input_data:
# Check whether character is present in the dictionary. If not then add to the dictionary
    if s in frequency:
        frequency[s] += 1
    else:
        frequency[s] = 1

# for key, value in frequency.items():
#   print(key, value)

max_char = max(frequency, key=frequency.get)
print("Maximum frequency character in string is:", max_char)
