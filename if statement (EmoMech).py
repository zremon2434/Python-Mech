# Project: If statement
# Author: Emon

# Get and display the initial math result input
mathresult = input('Emon your result is published. Please type your maths result ')
print('My maths result is ', mathresult)

# Get a new math score input and calculate the remainder when divided by 2
z = float(input('Enter your math score again '))
score = z % 2

# Check if the score is even and print the corresponding message
if score == 0:
    print('Your score is an even number.')

# Check if the score is odd and print the corresponding message
if score != 0:
    print('Your score is an odd number.')

