from collections import deque

def tomato_ripeness(box):
    # 상하좌우 이동 방향
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque()

    # 초기 익은 토마토 위치를 큐에 추가
    for i in range(len(box)):
        for j in range(len(box[0])):
            if box[i][j] == 1:
                queue.append((i, j, 0))

    # BFS 수행
    while queue:
        x, y, days = queue.popleft()

        # 상하좌우로 이동하며 익지 않은 토마토를 익게 만듦
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(box) and 0 <= ny < len(box[0]) and box[nx][ny] == 0:
                box[nx][ny] = 1
                queue.append((nx, ny, days + 1))

    # 모든 토마토가 익은 상태인지 확인
    for row in box:
        if 0 in row:
            return -1  # 익지 않은 토마토가 남아있다면 -1 반환

    return days

# 상자의 크기 입력
M, N = map(int, input().split())

# 토마토 상태 입력
box = [list(map(int, input().split())) for _ in range(N)]

# 토마토 익음 여부 확인 및 최소 일수 계산
result = tomato_ripeness(box)

# 결과 출력
print(result)
