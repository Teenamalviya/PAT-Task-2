# Problem: 1

'''write a program to calculate the total numbers of vowels and
count of each individual vowel A,E,I,O,U in the string "Guvi Geeks Network Private Limited'''

# Declaring the variable and assigning the string into it
stringvalue = "Guvi Geeks Network Private Limited"

#Print string given in problem statement
print("Given String:",stringvalue)

#Declare counters for each vowels
counta = 0
counte = 0
counti = 0
counto = 0
countu = 0

# Run for loop on the given string inorder to get each character from given string
for value in stringvalue:
   #Compare each character with vowels(a,e,i,o,u)
   if value == 'a' or value=='A':
        counta = counta+1
   if value == 'e' or value=='E':
       counte = counte+1
   if value == 'i' or value=='I':
       counti = counti+1
   if value == 'o' or value=='O':
       counto = counto+1
   if value == 'u' or value=='U':
       countu = countu+1

# Summation of all vowels
totalvowels = counta+counte+counti+counto+countu

#Print total number of vowels and number of each vowel present in the string
print("Total number of vowels in a given string:",totalvowels)
print("Number of vowel A:",counta,"\nNumber of vowel E:",counte,"\nNumber of vowel I:",counti,"\nNumber of vowel O:",counto,"\nNumber of vowel U:",countu)

