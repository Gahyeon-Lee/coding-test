# 같은 숫자는 싫어(level 1)

def solution(arr):
    b = []
    for i in range(len(arr)):
        if i == 0:
            b.append(arr[i])
            print(b)
        elif arr[i] != arr[i-1]:
            b.append(arr[i])

    return b

arr = [1,1,1,3,3,0,1,1]

print(solution(arr))