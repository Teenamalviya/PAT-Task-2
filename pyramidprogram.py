# Problem: 2

# Create a pyramid of numbers from 1 to 20 using for loop:

#The maximum limit of the number
num = 20
# Using For Loop
for first in range(num,0,-1):
    print(*[" "]*(first-1),*range(first,num),*range(num,first-1,-1))
