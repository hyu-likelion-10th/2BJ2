alphabets = [0 for i in range(52)]

word = input()
for char in word:
    if 'a' <= char and char <= 'z':
        alphabets[ord(char)-ord('a')] += 1
    else :
        alphabets[ord(char)- ord('A')+26] += 1

result = ""
maxCnt = -1
isDupliacate = False
for i in range(26):
    currCnt = alphabets[i] + alphabets[i+26]
    if maxCnt < currCnt :
        maxCnt = currCnt
        result = chr(ord('A') + i)

for i in range(26):
    currCnt = alphabets[i] + alphabets[i+26]
    if currCnt == maxCnt and chr(ord('A') + i) != result:
        isDupliacate = True
        
if isDupliacate :
    print("?")
else :
    print(result)