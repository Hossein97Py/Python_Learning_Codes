#How to round the number and then show it?
#test with 150-5-12

print('Wellcome to the tip calculater')
TotalBill = float (input('How much was the toal bill? '))
People = int (input('How many people to split the bill? '))
Percentage = int(input ('What percentage of the bill are you willing to tip? 10, 12 or 15? '))

Pay = (TotalBill * (1 + Percentage / 100)) / People

##########################################################################
#Pay_final = round(Pay, 2)
Pay_final = "{:.2f}".format(Pay) #This convert the floating number to the string that abide by that format
##########################################################################
print (f'Each person should pay: {Pay_final} ')

#1400/03/24
