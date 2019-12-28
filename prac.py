game_size = 3

print("   0  1  2")
'''
s = "   "
for i in range(game_size):
	s += str(i)+"  "
print(s)
'''
s = "   "+"  ".join([str(i) for i in range(game_size)])
print(s)
'''
for i in range(game_size):
	row=[]
	for i in range(game_size):
		row.append(0)
	game.append(row)

print(game)'''

'''
game_size = input("what size game of tic tac toe")
game = [[0 for i in range(game_size)] for i in range(game_size)]
print(game)
'''










'''
a = 'Hello world whats up'
lookfor = 'world'

print(a[a.find(lookfor):19])

#See if the string starts with a capital letter
print(a.istitle())

# Making every first character of the string capitalize
print(a.title())

# splitting the string into single characters
print(list(a))

# Making all the strings capitalize
print(a.upper())

# Checking if the string is capatilize
print(a.isupper())

print(a.swapcase())



def LetterChanges(str): 

    str = list("hello*3")
    
    for i in range(len(str)):
        str.append(str[i+1])
    return str
    
# keep this function call here  
print (LetterChanges(str))


'''