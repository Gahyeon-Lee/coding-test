# 저작권
# 첫째 줄에 앨범에 수록된 곡의 개수 A와 평균값 I가 주어진다. (1 ≤ A, I ≤ 100)
# 첫째 줄에 적어도 몇 곡이 저작권이 있는 멜로디인지 출력한다.

average, song_num = map(int, input().split())

print(average * (song_num - 1) + 1)