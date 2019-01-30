game = [[2,0,1],
		[2,0,0],
		[2,0,0],]


for col in range(len(game)):
	check=[]
	for row in game:
		check.append(row[col])

	if check.count(check[0]) == len(check) and check[0] != 0:
			print('winner')


'''
def win(current_game):
	for row in game:
		print(row)
		if row.count(row[0]) == len(row) and row[0] != 0:
			print('winner')

win(game)
'''



'''def game_board(player=0,row=0, column=0, just_dislapy=False):
	try:
		print('  0  1  2')
		if not just_dislapy:
			game[row][column]= player
		for count, row in enumerate(game):
			print(count,row)
	except IndexError as e:
		print("Error: ",e)
	except Exception as e:
		print("Something went wrong", e)

game = game_board(just_dislapy=True)
game =game_board(2,4,1)'''




'''game = [1,2,3]


def game_board(player=0,row=0, column=0, just_dislapy=False):
	game = "A game"
	print(game)


game_board(game)
print(game)'''