from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer



# def solution(n, weak, dist):
#     answer, num, data, result = 0, 1, [0] * (n*2), []
#     for i in range(len(dist)):
#         dist[i] = dist[i] + 1
#     dist.sort(reverse=True)
    
#     # 원형을 일자로 펴서 같은 것을 하나 더 붙이고 weak 정의
#     for i in range(len(weak)):
#         data[weak[i]] = weak[i]
#         data[weak[i]+n] = weak[i]
    
#     # dist 높은 숫자부터
#     for i in dist:
#         total = []
#         answer += 1
#         for j in range(n*2):
#             front, back = [], []
#             # dist의 수만큼 앞으로 전진
#             for k in range(i):
#                 # dist에서 weak를 커버할 수 있는지
#                 now = j + k
#                 if now >= n*2:
#                     break
#                 elif data[now] > 0:
#                     front += [data[now]]
#             # dist의 수만큼 뒤로 전진
#             for k in range(i):   
#                 now = j - k
#                 if now < 0:
#                     break
#                 elif data[now] > 0:
#                     back += [data[now]]
#             # 시계방향으로 같은 값이 없거나 0인 아닌 경우
#             if front not in total and len(front) != 0:
#                 total += [front]
#             # 반시계방향
#             if back not in total and len(back) != 0:
#                 total += [back]
#         result += [total]
        
#         # 2개씩 비교
#         if len(result) == 2:
#             num, plus = [], []
#             for a in range(len(result[0])):
#                 for b in range(len(result[1])):
#                     plus = result[0][a] + result[0][b]
#                     plus.sort()
#                     if plus not in num:
#                         num += [plus]
#             # deepcopy를 써야 함, 현재는 주소 복사됨
#             result = [num]
        
#         for r in result[0]:
#             # 중복 제거 및 오름차순 정렬
#             r = list(set(r))
#             r.sort()
#             # weak를 모두 해결했으면 return
#             if r == weak:
#                 return answer
