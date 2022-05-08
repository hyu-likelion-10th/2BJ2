tc = int(input())

for i in range(tc) :
    info = list(map(int, input().split()))
    n = info[0]
    scores = info[1:]
    avg = sum(scores) / n
    overAvgCnt = 0
    for score in scores :
        if score > avg :
             overAvgCnt += 1
    result = (overAvgCnt / n) * 100
    print(f"{result:.3f}%")