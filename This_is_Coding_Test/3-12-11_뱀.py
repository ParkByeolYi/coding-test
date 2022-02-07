n = int(input())
k = int(input())
apple, rotation = [], []
apple += [list(map(int, input().split())) for _ in range(k)]
l = int(input())
rotation += [list(input().split()) for _ in range(l)]

# snake, snake_rotate, direction, cnt, (x, y), last
# 뱀, 뱀 'L' or 'D', (동, 1: 남, 2: 서, 3: 북), 몇 초, 뱀이 앞으로 갈 위치(머리 위치), 마지막으로 꼬리가 있었던 위치
snake, snake_rotate, direction, cnt, x, y, last = [], "", 0, 0, 0, 0, [0, 0]

# 뱀 머리 위치가 보드 밖으로 나가면 break
while 0 <= x <= n-1 and 0 <= y <= n-1:
  cnt += 1

  # 왼쪽, 오른쪽으로 방향을 바꿈
  if snake_rotate != "":
    if snake_rotate == "L":
      if direction == 0: direction = 3
      elif direction == 1: direction = 0
      elif direction == 2: direction = 1
      elif direction == 3: direction = 2

    elif snake_rotate == "D":
      if direction == 0: direction = 1
      elif direction == 1: direction = 2
      elif direction == 2: direction = 3
      elif direction == 3: direction = 0
  
  # 현재 direction에 따라 x, y값 이동
  if direction == 0: y += 1
  elif direction == 1: x += 1
  elif direction == 2: y -= 1
  elif direction == 3: x -= 1

  # direction은 유지한채 snake_rotate은 삭제
  snake_rotate = ""
  # 뱀의 머리 부분 추가
  snake.append([x, y])
  
  # 뱀의 몸에 닿았는지 확인
  snake_copy = list(set(map(tuple, snake)))
  if len(snake) != len(snake_copy):
    break
  # 뱀의 꼬리와 머리가 닿았는지 확인
  if last == [x, y]:
    break
  
  # 사과가 있으면
  if len(apple) > 0:
    for i in range(len(apple)):
      # 사과의 좌표와 현재 머리의 위치가 같으면
      if x == apple[i][0]-1 and y == apple[i][1]-1:
        # 사과 없앰
        apple.remove(apple[i])
        break
      # 모두 검사했는데 사과 없으면
      if i == len(apple)-1:
        # 뱀의 꼬리 삭제
        last = snake.pop(0)
  else:
    # 뱀의 꼬리 삭제
    last = snake.pop(0)

  # 방향 바꿀 초가 되면 (순서대로 정보가 주어짐))
  if len(rotation) > 0 and int(rotation[0][0]) == cnt:
    # 뱀의 방향 바꾸기
    snake_rotate = rotation[0][1]
    rotation.remove(rotation[0])

print(cnt)
