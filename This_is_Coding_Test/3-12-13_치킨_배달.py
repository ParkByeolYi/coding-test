import itertools

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
house, chicken = [], []

# 집과 치킨집의 좌표를 튜플로 저장한다.
for i in range(n):
	for j in range(n):
		if data[i][j] == 1:
			house.append((i, j))
		elif data[i][j] == 2:
			chicken.append((i, j))

# 폐업시켜야 할 치킨집이 없는 경우
if len(chicken) == m:
	# 현재 치킨 거리, 한 집의 가장 작은 치킨 거리, 최종 출력(모든 집의 가장 작은 치킨 거리의 합)
	now, answer, result = 0, 1e9, 0
	for i in range(len(house)):
		for j in range(len(chicken)):
			r1, c1 = house[i]
			r2, c2 = chicken[j]
			now = abs(r1-r2) + abs(c1-c2)
			answer = min(answer, now)
		result += answer
		answer = 1e9

# 폐업시켜야 할 치킨집이 있는 경우
else:
	# 현재 치킨 거리, chicken_comb가지 m개 중에서 한 집의 가장 작은 치킨 거리, comb에서 모든 집의 가장 작은 치킨 거리의 합, 최종 출력(chicken_comb 중에서 모든 집의 가장 작은 치킨 거리의 합)
	now, answer, final, result = 0, 1e9, 0, 1e9
	# 조합 사용
	chicken_comb = list(itertools.combinations(chicken, m))

	# chicken_comb가지
	for comb in range(len(chicken_comb)):
		# 집 접근
		for i in range(len(house)):
			# chicken_comb가지 중 m개씩 접근
			for j in range(m):
				r1, c1 = house[i]
				r2, c2 = chicken_comb[comb][j]
				now = abs(r1-r2) + abs(c1-c2)
				answer = min(answer, now)
			final += answer
			answer = 1e9
		result = min(result, final)
		final = 0

print(result)
