import random

letter = int (input('How many letter do you want in your password?\n'))
symbol = int(input('How many symbol do you want in your password?\n'))
number = int (input('How many number do you want in your password?\n'))

letter_list = ['a','b', 'c','d','e','f','g','h','i','j',
'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #26 member
symbol_list = ['~','!','@','#','$','%','^','&','*','(',')','_','+'] #13 member

TotalLength = letter + symbol + number
password = []

letter_used = symbol_used = number_used = 0

while len(password) < TotalLength:
    type = random.randint(0,2)
    if type == 0 and letter_used < letter:
        put_number = random.randint(0,25)
        password.append(letter_list[put_number])
        letter_used += 1
    elif type == 1 and symbol_used < symbol:
        put_number = random.randint(0,12)
        password.append(symbol_list[put_number])
        symbol_used += 1
    elif type == 2 and number_used < number:
        password.append(str(random.randint(0,9)))
        number_used += 1

password_string = str()
for j in range( len(password)):
    password_string = password_string + password[j]

password_string.rstrip()
print (password_string)

#1400/03/25
