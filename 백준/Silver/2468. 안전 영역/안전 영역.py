n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

waters = []
for i in range(n):
    for j in range(n):
        if graph[i][j] not in waters:
            waters.append(graph[i][j])

# 노트: 아무 지역도 물에 잠기지 않을 수도 있다. 지역의 높이는 1부터 시작하므로 아무 지역도 물에 잠기지 않으려면 비의 양이 0인 경우 고려 
waters.append(0)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque


def count_safety(visited, water):
    group_count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > water and visited[i][j] == 0:
                group_count += 1
                q = deque()
                q.append((i, j))
                visited[i][j] = 1

                while q:
                    x, y = q.popleft()
                    for k in range(4):  # 인덱스 변수명 주의! i 위에서 사용함
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > water and visited[nx][ny] == 0:
                            q.append((nx, ny))
                            visited[nx][ny] = 1
    return group_count


max_value = 0
for water in waters:
    # 높이가 water 일 때 안전 영역 구하기
    visited = [[0 for _ in range(n)] for _ in range(n)]  # 2차원 배열 초기화
    count = count_safety(visited, water)
    if max_value < count:
        max_value = count

print(max_value)
