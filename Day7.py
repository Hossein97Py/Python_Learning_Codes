import random

word_list = ['banana', 'apple', 'orange', 'grape', 'melon', 'cherry']
word = word_list[random.randint(0, len(word_list)-1)]
user_word = '-' * len(word) ;print (user_word)

i = 0
while True:
	user_letter = input ('Please input the letter:\n')
	if user_letter in word:
		x = 0 #The index of the letter matched
		for letter in word:
			if letter == user_letter:
				user_word = user_word[:x] + letter + user_word[x+1:]
			x += 1
		print (user_word)
	i += 1
	print (f'you have {7 - i} tries left')
	if '-' not in user_word:
		print ('You Won !!!!!!!!!!!!!!!!!!!')
		break
	elif i > 6:
		print ('You Lost !!!!!!!!!!!!!!!!!!!')
		break
	else:
		continue
#1400/03/27	All by myself (With the help of book and the internet)
