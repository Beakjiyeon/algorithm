from collections import deque

n, m = map(int, input().split())
table = [list(input()) for _ in range(m)]

# 상, 우, 좌, 하 - x, y 반대라 생각
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방문 정보 기록용
visited = [[False] * n for _ in range(m)]


def move(i, j, color):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    count = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if table[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    return count


white_result, black_result = 0, 0
# 순회 하면서 색깔 뭉치 카운트
for i in range(m):
    for j in range(n):
        if table[i][j] == 'W' and not visited[i][j]:
            white = move(i, j, 'W') + 1  # 시작 좌표 더하기
            white_result = white_result + white ** 2
        elif table[i][j] == 'B' and not visited[i][j]:
            black = move(i, j, 'B') + 1
            black_result = black_result + black ** 2
print(white_result, black_result)
