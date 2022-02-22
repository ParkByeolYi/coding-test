import sys
input = sys.stdin.readline

n = int(input())
km = list(map(int, input().split()))
oil = list(map(int, input().split()))
num, price, result = km[0], oil[0], 0

for i in range(n-1):
    # 지금까지 나온 주유값이 이번 주유값보다 작으면
    if price <= oil[i]:
        # 가야하는 km를 더함
        if i != 0 and i <= len(km)-1:
            num += km[i]
    else:
        # 거리와 가격을 곱해서 더함
        result += num * price

        # 현재 갈 거리와 기름값으로 초기화함
        if i <= len(km)-1:
            num = km[i]
        if i <= len(oil)-1:
            price = oil[i]

    # 마지막으로 거리와 가격을 곱해서 더함
    if i == n-2:
        result += num * price

# 비용 출력
print(result)
