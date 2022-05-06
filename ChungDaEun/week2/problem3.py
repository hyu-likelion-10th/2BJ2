import operator

word = input()
dic= {}

for alphabet in word:
    alphabet = alphabet.upper()
    if alphabet in dic:
        dic[alphabet] += 1
    else:
        dic[alphabet] = 1
sortedDic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)

if (len(word) == 1 or sortedDic[0][1] != sortedDic[1][1]):
    print(sortedDic[0][0])
else:
    print('?')
