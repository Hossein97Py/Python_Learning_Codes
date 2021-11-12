#This could be solved way easier without using the dictionary HKh

import os
os.system('clear')
print ('Wellcome to the auction!')
biderDic = dict()
#Creating the dictionary
while True:
    name = input('Please input your name:\n')
    bid = float (input('How much is your bid?\n$'))
    cond = input('Is there any one else? ("y" for yes and "n" for no)\n')
    biderDic[name] = bid
    if cond == 'y':
        os.system('clear') #for runing in gitbash or linux. for windows it is os.system('cls').
    else:
        break
#Creating the list
os.system('clear')
biderList = list()
i = 0 ; j = 1
#print (biderDic.items())
for k, v in biderDic.items():
    biderList.append(k)
    biderList.append(v)
    i +=1 ; j += 1
#print (biderList)
#Retriving the highest value
highvalue = 0
for i in range (1, len(biderList), 2):
    value = biderList[i]
    if value > highvalue:
        highvalue = value
        high_index = i

print (f'The winner is {biderList[high_index-1]} with the bid of {biderList[high_index]}$')

#1400/03/08
