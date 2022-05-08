def solution(participant, completion):    
    participant.sort()
    completion.sort()
    
    for idx in range(len(completion)):
        if completion[idx] != participant[idx]:
            return participant[idx]
    return participant[len(participant)-1]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
