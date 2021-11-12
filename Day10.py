def calculator(operator, a, b):
    if operator == '+':
        return (a+b)
    elif operator == '-':
        return (a-b)
    elif operator == '*':
        return (a*b)
    elif operator == '/':
        return (a/b)

a = float(input('input the first number:\n'))
while True:
    operator = input('which operate do you wanna use?\n+\n-\n*\n/\n')
    b =float(input('input the second number:\n'))
    c = calculator(operator, a, b)
    print(c)
    cont = input('Do you want to continue with this result? ("y" or "n")\n')
    if cont == 'n':
        break
    elif cont == 'y':
        a = c
        continue

#1400/03/28
