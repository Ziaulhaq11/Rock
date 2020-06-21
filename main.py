import random

player_1 = input("Enter 'r' for rock 'p' for paper 's' for scissor : ")

def random_no():
	player_2 = random.randint(1,3)
	return player_2

if player_1.lower() == 'r':
	other = random_no()
	if other == 1:
		print('draw')
	elif other == 2:
		print('You lost')
	elif other == 3:
		print('You won')

elif player_1.lower() == 'p':
	other = random_no()
	if other == 1:
		print('You win')
	elif other == 2:
		print('draw')
	elif other == 3:
		print('You lost')

elif player_1.lower() == 's':
	other = random_no()
	if other == 1:
		print('You lost')
	elif other == 2:
		print('You win')
	elif other == 3:
		print('draw')

else:
	print('enter correctly')


	