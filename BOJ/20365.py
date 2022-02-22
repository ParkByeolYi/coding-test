import sys
input = sys.stdin.readline

n = int(input())
color = list(input())
# 마지막 요소로 개행문자가 들어가서 삭제함
color.pop()

# 색상이 몇 번 연속되었는지, 같은 색상의 묶음이 몇 개인지, 최종 답안
countR, countB, red, blue, result = 0, 0, 0, 0, 0

for c in color:
    if c == 'R':
        countB = 0
        
        if countR > 0:
            countR += 1
        else:
            red += 1
            countR += 1
            
    elif c == 'B':
        countR = 0
        
        if countB > 0:
            countB += 1
        else:
            blue += 1
            countB += 1

if red >= blue:
    result = blue + 1
else:
    result = red + 1
    
print(result)
