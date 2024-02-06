from collections import deque

n = int(input())

mx = [-2, -2, 2, 2, -1, -1, 1, 1]
my = [-1, 1, -1, 1, -2, 2, -2, 2]


def sol(graph, start, destination):
    queue = deque()
    queue.append(start)

    visited = [[0] * len(graph) for _ in range(len(graph))]
    visited[start[0]][start[1]] = 1
    while queue:
        x, y = queue.popleft()

        if (x, y) == destination:
            return visited[x][y] - 1
        for i in range(8):
            nx = x + mx[i]
            ny = y + my[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph):
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


for _ in range(n):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    sx, sy = map(int, input().split())
    dx, dy = map(int, input().split())

    print(sol(graph, (sx, sy), (dx, dy)))
