print ('Welcome to the tressure island. Your mission is to find the tressure')
one = input('You`re some where now. Do you wanna go "left" or "right" ?\n').lower()
if one == 'right':
    print ('game over!!!')
elif one == 'left':
    two = input ('Okay, you went left. Now do you "wait" for a boat or rather "swim" ?\n').lower()
    if two == 'swim':
        print ('game over!!!')
    elif two == 'wait':
        three = input ('Yo`ve reached someplace good. which door do you go in? "blue", "red" or "yellow" ?\n').lower()
        if three == 'yellow':
            print ('You Won !!!!!!!!!!')
        elif three == 'blue' or 'red':
            print ('game over!!! three')

        else:
            print ('Try again')

    else:
        print ('Try again')

else:
    print ('Try again')

#1400/03/24
