n, k = map(int, input().split())
data = [i+1 for i in range(n)]
num, result = 0, []

for i in range(n):
    num += k-1
    if num >= len(data):
        num %= len(data)

    result.append(str(data.pop(num)))

print("<", ", ".join(result)[:], ">", sep="")



"""
# 처음 작성한 코드
from collections import deque

n, k = map(int, input().split())
graph, num, result = [], k, []

for i in range(n):
    graph.append(i+1)

q = deque(graph)

while q:
    result.append(q.pop(3))
    num += k

print("<", end="")
for i in range(len(result)):
    if i == n-1:
        print(result[i], end=">")
    else:
        print(result[i], end=", ")
"""
