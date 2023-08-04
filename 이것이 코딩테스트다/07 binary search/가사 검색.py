# 가사 검색
# 난이도 3 | 풀이 시간 1시간 30분 | 시간 제한 1초 | 메모리 제한 128MB

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
        
    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer 