# 1343.py
# 폴리오미노

board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)
    
# 길이가 가장 긴 4문자 XXXX를 AAAA로 바꿔줌
# 다음으로 긴 2문자 XX를 BB로 바꿔줌
# 왜 이렇게 어렵게 돌려서 생각했을까...바보...멍청이 