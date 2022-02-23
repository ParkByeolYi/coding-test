import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

# 내림차순으로 정렬
crane.sort(reverse=True)
box.sort(reverse=True)

result = -1
# 답은 m을 초과하는 수가 나올 수 없다.
for i in range(m):
    # 1분에 모든 크레인은 동시에 움직임
    for j in range(n):
        # 남은 박스 수만큼 반복
        for k in range(len(box)):
            # 무게 제한을 넘지 않는다면
            if crane[j] >= box[k]:
                box.remove(box[k])
                # remove를 pop으로 대체 가능
                # box.pop(k)
                break
    # 박스를 다 옮겼으면
    if len(box) == 0:
        # 걸린 시간 (분 단위)
        result = i+1
        break

print(result)
