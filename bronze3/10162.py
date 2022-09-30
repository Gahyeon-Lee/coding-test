# 전자레인지
# 첫 번째 줄에는 요리시간 T(초)가 정수로 주어져 있으며 그 범위는 1 ≤ T ≤ 10,000 이다. 
# 여러분은 T초를 위한 최소버튼 조작의 A B C 횟수를 첫 줄에 차례대로 출력해야 한다. 
# 각각의 횟수 사이에는 빈 칸을 둔다. 해당 버튼을 누르지 않는 경우에는 숫자 0을 출력해야한다. 
# 만일 제시된 3개의 버튼으로 T초를 맞출 수 없으면 음수 -1을 첫 줄에 출력해야 한다. 

A = 300
B = 60
C = 10

time = int(input())

if time % C > 0:
    print(-1)
else:
    if time >= A:
        button_A = time // A
        button_B = (time % A) // B
        button_C = ((time % A) % B) // C
    elif time < A:
        button_A = 0
        button_B = time // B
        button_C  = (time % B) // C
    elif time < B:
        button_A = 0
        button_B = 0
        button_C = time // C

    print(button_A, button_B, button_C)
