import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 매서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)



"""
# 60분 동안 작성한 코드
from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 바이러스를 퍼트리는 부분
def dfs(graph, x, y, visited):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        elif visited[nx][ny] == 1:
            continue
        elif visited[x][y] == 2:
            visited[nx][ny] = 2
            dfs(graph, nx, ny, visited)

    return visited

visited = deepcopy(graph)

# 벽을 세우는 부분
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(n):
            for y2 in range(m):
                for x3 in range(n):
                    for y3 in range(m):
                        if graph[x1][y1] == 0 and graph[x2][y2] == 0 and graph[x3][y3] == 0 and x1 != x2 != x3 and y1 != y2 != y3:
                            visited = deepcopy(graph)
                            visited[x1][y1], visited[x2][y2], visited[x3][y3] = 1, 1, 1
                            
                            print()
                            print(x1, y1, x2, y2, x3, y3)
                            print(visited)
                            for x in range(n):
                                for y in range(m):
                                    if visited[x][y] == 2:
                                        dfs(graph, x, y, visited)                
"""
