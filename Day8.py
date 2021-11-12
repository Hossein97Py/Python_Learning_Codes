way = input ('Do you want to "encode" or "decode" a phrase?\n')
user_word = input ('Please type the word:\n')
shift_number = int(input('Please input the shift number:\n'))
letter = ['a','b','c','d','e','f','g','h','i','j','k','l',
'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

coded_letter_list = list()
for i in range (26 - shift_number):
    coded_letter_list.append( letter[i + shift_number])
for j in range (shift_number):
    coded_letter_list.append( letter[j])
#print ('coded_letter_list:\n', coded_letter_list)
decoded_letter_list = list()
for i in range (shift_number):
    decoded_letter_list.append( letter[26 - shift_number + i])
for j in range (shift_number , 26):
    decoded_letter_list.append( letter[j - shift_number])
#print ('decoded_letter_list:\n', decoded_letter_list)

coded_word = list()
if way == 'encode':
    user_word = list(user_word)
    for l in user_word:
        coded_word.append(coded_letter_list[letter.index(l)])
    output = ''.join(coded_word)
    print ('The coded massage is:\n' + output)

elif way == 'decode':
        user_word = list(user_word)
        for l in user_word:
            coded_word.append(decoded_letter_list[letter.index(l)])
        output = ''.join(coded_word)
        print ('The decoded massage is:\n' + output)

#1400/03/28
