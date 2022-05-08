def solution(participant, completion):
    dict = {name : 0 for name in participant }
    for p in participant:
        dict[p] += 1
    for c in completion:
        dict[c] -= 1
    for k, v in dict.items():
        if v > 0 :
            answer = k
            break
    return answer