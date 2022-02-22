import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x:(x[1], x[0]))
result, now = 1, 0

for i in range(1, n):
	if data[now][1] <= data[i][0]:
		result += 1
		now = i

print(result)



"""
# 처음 작성한 코드
import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort()
result = 0

for i in range(n):
	now, finish = 0, data[i][1]
	for j in range(i+1, n):
		if finish < data[j][0]:
			now += 1
			finish = data[j][0]
	result = max(now, result)

print(result)
"""
