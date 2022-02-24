from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])



"""
# 처음 작성한 코드
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def virus(x, y, now):
    # 현재 바이러스의 종류
    num = graph[x][y]

    # 오름차순으로 번식하는지 확인
    if num == now:
        # 상, 하, 좌, 우로 바이러스가 퍼짐
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            elif graph[nx][ny] == 0:
                graph[nx][ny] = num
        return now + 1
    return now

def dfs(cnt, x, y, now):
    # 2중 for문의 반복 순서대로 번호가 나오지 않을 경우 -> 비효율적인 방법
    for _ in range(k):
        for a in range(n):
            for b in range(n):
                now = virus(a, b, now)
                if now == k + 1: now = 1
            
    cnt -= 1
    if cnt == 0: return
        
dfs(s, 0, 0, 1)

print(graph[x-1][y-1])
"""
