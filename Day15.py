# The Coffee Machine Project
resource = {
    'Water': 300,
    'Milk': 200,
    'Coffee': 100,
    'Money': 0
}

while True:
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    for k, v in resource:
        print(k, v)
    if coffee == 'report':
        for k, v in resource:
            print(k, v)

    #elif coffe == espresso:

