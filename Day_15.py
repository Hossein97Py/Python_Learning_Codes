resources = {
    'Water': 300,
    'Milk': 200,
    'Coffee': 100,
    'Money': 0
}

class Coffee:
    def espresso():
        resources['Water'] -= 50
        resources['Coffee'] -= 18
        resources['Money'] += 1.5

    def latte():
        resources['Water'] -= 200
        resources['Coffee'] -= 24
        resources['Milk'] -= 150
        resources['Money'] += 2.5

    def cappuccino():
        resources['Water'] -= 250
        resources['Coffee'] -= 24
        resources['Milk'] -= 100
        resources['Money'] += 3

class Sufficient:
    def espresso():
        if resources['Water'] < 50:
            print('Sorry there is not enough water.')
            return False
        elif resources['Coffee'] < 18:
            print('Sorry there is not enough coffee.')
            return False
        else:
            return True
    def latte():
        if resources['Water'] < 200:
            print('Sorry there is not enough water.')
            return False
        elif resources['Coffee'] < 24:
            print('Sorry there is not enough coffee.')
            return False
        elif resources['Milk'] < 150:
            print('Sorry there is not enough milk.')
            return False
        else:
            return True

    def cappuccino():
        if resources['Water'] < 250:
            print('Sorry there is not enough water.')
            return False
        elif resources['Coffee'] < 24:
            print('Sorry there is not enough coffee.')
            return False
        elif resources['Milk'] < 100:
            print('Sorry there is not enough milk.')
            return False
        else:
            return True

while True:
    coffee = input('What Would You Like?\n1_espresso\n2_latte\n3_cappuccino\n')
    if coffee == '1':
        x = Sufficient.espresso()
        if x:
            Coffee.espresso()
    elif coffee == '2':
        x = Sufficient.latte()
        if x:
            Coffee.latte()
    elif coffee == '3':
        x = Sufficient.cappuccino()
        if x:
            Coffee.cappuccino()
    elif coffee == 'report':
        print(resources)
    elif coffee == 'off':
        break




