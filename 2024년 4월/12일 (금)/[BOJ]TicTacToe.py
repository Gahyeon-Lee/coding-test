# 13227.py
# TicTacToe

board = []
for _ in range(3):
    board.append(list(map(str, input())))

check = False
for i in range(3):
    now = board[0][i]
        
    if board[1][i] == now and board[2][i] == now and now != '.':
        check = True

for i in range(3):
    now = board[i][0]
        
    if board[i][1] == now and board[i][2] == now and now != '.':
        check = True

if board[0][0] == board[1][1] and board[2][2] == board[1][1] and board[1][1] != '.':
        check = True
elif board[0][2] == board[1][1] and board[2][0] == board[1][1] and board[1][1] != '.':
        check = True

if check:
    print('YES')
else:
    print('NO')