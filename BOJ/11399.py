import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
data = []

for a in range(n):
	data.append((a+1, time[a]))
data.sort(key=lambda x:x[1])

now, result = 0, 0
for a in range(n):
	now += data[a][1]
	result += now

print(result)



"""
# 다른 분의 풀이
n = int(input())
s = list(map(int, input().split()))
num = 0
s.sort()
for i in range(n):
    for j in range(i + 1):
        num += s[j]
print(num)
"""
