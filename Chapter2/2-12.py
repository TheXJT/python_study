board=[['_']*3 for i in range(3)]
board=[]
for i in range(3):
	row=['_']*3
	board.append(row)
print(board)
board[2][0]='X'
print(board)