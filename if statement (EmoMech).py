mathresult = input(
    'Emon your result is published. Please type your maths result ')
print('My maths result is ', mathresult)

z = float(input('enter your math score again '))
score = z % 2

if (score == 0):
    print('your score is an even number.')

if (score != 0):
    print('your score is an odd number.')
