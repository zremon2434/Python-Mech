frompc = float(input('Please tell me your physics score last day '))

print('Emon your score is', frompc)

score = frompc % 2
if (score == 0 and frompc > 0):
    print('Your score is positive even.')

if (score == 0 and frompc < 0):
    print('Your score is negative even.')

if (score != 0 and frompc > 0):
    print('Your score is positive odd.')

if (score != 0 and frompc < 0):
    print('Your score is negative odd.')

if (frompc == 0):
    print('Your score Zero.Too bad.')
