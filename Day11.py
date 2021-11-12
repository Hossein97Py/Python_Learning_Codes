
print ('********************Wellcome to the BlackJack game********************')
import random

usercard = [random.randint(1,10)]
computercard = [random.randint(1,10)]

while True:
    usercard.append(random.randint(1,10))
    computercard.append(random.randint(1,10))
    print (f'one of the computer card is: {computercard[0]}')
    print (f'Your cards are: {usercard}')
    con = input('Do you want to continue? ("y" or "n")')
    if con == 'n':
        break
    if sum(usercard) > 21:
        print("You Bust")
        print (f'Your cards are: {usercard}')
        break

if (21 - sum(usercard)) <= (21 - sum(computercard)):
        print('You Won!!!')
        print (f'Your cards are: {usercard}')
        print (f'Computers cards are: {computercard}')
else:
        print ('You Lost!!!')
        print (f'Your cards are: {usercard}')
        print (f'Computers cards are: {computercard}')
