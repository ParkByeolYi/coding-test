from collections import deque
import sys
input = sys.stdin.readline

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)



"""
# for문으로 구현한 코드
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [0] * (n+1)

for i in range(m):
    if x == graph[i][0]:
        visited[graph[i][1]] = 1
    elif visited[graph[i][0]] != 0 and (visited[graph[i][1]] == 0 or visited[graph[i][1]] > visited[graph[i][0]] + 1):
        visited[graph[i][1]] = visited[graph[i][0]] + 1
    print(visited)

cnt = 0

for i in range(len(visited)):
    if visited[i] == k:
        print(i)
    else:
        cnt += 1
        
if cnt == len(visited):
    print(-1)
"""



"""
# 처음 작성한 코드
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

print(graph)

def dfs(graph, x, visited):
    visited[x] = 0
    
    for a, b in graph:
        if a == 1:
            visited[b] = 1
        else:
            if visited[a] != 0 and (visited[b] == 0 or visited[a] + 1 <= visited[b]):
                visited[b] = visited[a] + 1

visited = [0] * (n+1)
dfs(graph, x, visited)

result = []

for v in visited:
    if v == k:
        result.append(v)

print(result, end="/n")
"""



"""
# DFS 예제
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1,  7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
"""
