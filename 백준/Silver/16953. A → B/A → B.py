from collections import deque
a, b = map(int, input().split())
q = deque()
q.append((a, 0))

count = 0
while True:
    # 큐가 완전히 빌 때까지 동작 == a에서 만들 수 없는 케이스
    if len(q) == 0:
        print(-1)
        break
        
    now, count = q.popleft()
    if now == b:
        print(count + 1)
        break
        
    # 케이스 줄이기
    if now > b:
        continue

    q.append((now * 2, count + 1))
    q.append((int(str(now) + '1'), count + 1))