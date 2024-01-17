# Problem: 6

# Enter first and second string
str1 = input("Enter your first string : ")
str2 = input("Enter your second string : ")
#Assign empty string to the variable
longestString = ""
maxLength = 0
#Looping over the first string
for i in range(0, len(str1)):
#Compare elements of first string with the second string
    if str1[i] in str2:
#Looping over the first string from second element
        for j in range(i + 1, len(str1)):
#Compare substring with second string
            if str1[i:j] in str2:
                if(len(str1[i:j]) > maxLength):
                    maxLength = len(str1[i:j])
                    longestString = str1[i:j]
#Print the longest common substring
print(longestString)
