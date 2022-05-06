C = int(input())

answer = []
for i in range(C):
    score = list(map(int, input().split()))
    N = score[0]
    score = score[1:]
    avg = sum(score) / N
    overAvg = 0
    for j in score:
        if j > avg:
            overAvg += 1
    answer.append(overAvg / N * 100)

for i in answer:
    print(f'{i:.3f}%')
