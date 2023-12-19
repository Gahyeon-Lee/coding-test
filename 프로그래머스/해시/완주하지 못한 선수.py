# 완주하지 못한 선수

# 내가 푼 함수
def solution(participant, completion):
    answer = ''
    dict = {}
    
    for i in participant:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    for i in completion:
        if dict[i] != 0:
            dict[i] -= 1
    
    for key, value in dict.items():
        if value == 1:
            answer = key
    return answer

# 다른 사람들의 풀이
def solution2(participant, completion):
    hash_dict = {}
    sum_hash = 0
    
    for i in participant:
        hash_dict[hash(i)] = i
        sum_hash += hash(i)
        
    for i in completion:
        sum_hash -= hash(i)
        
    return hash_dict[sum_hash]

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]	

# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))
print(solution2(participant, completion))

# ここでも日本語書ける！！