def is_valid_index_x(x, m):
    if x < 0 or x >= m:
        return False
    return True


def is_valid_index_y(y, n):
    if y < 0 or y >= n:
        return False
    return True


if __name__ == '__main__':
    # 세로, 가로 길이
    n, m = map(int, input().split())

    # 각 노드가 연결된 정보가 담긴 그래프
    graph = []
    visited = [[] for _ in range(m)]

    for _ in range(n):
        graph.append(list(map(int, input())))

    from collections import deque
    queue = deque()
    queue.append((0, 0))

    while queue:
        y, x = queue.popleft()

        # 이미 방문한 곳을 가지 않도록 체크 해줘야 무한 반복을 하지 않는다.
        # right
        if is_valid_index_x(x + 1, m) and graph[y][x + 1] == 1:
            queue.append((y, x + 1))
            graph[y][x + 1] = graph[y][x] + 1 # 따로 visited 2차원 배열을 만들지 않고 graph에 값을 더하므로써 이미 방문한 노드를 안가는 것, 값 누적이 포인트

        # left
        if is_valid_index_x(x - 1, m) and graph[y][x - 1] == 1:
            queue.append((y, x - 1))
            graph[y][x - 1] = graph[y][x] + 1

        # top
        if is_valid_index_y(y - 1, n) and graph[y - 1][x] == 1:
            queue.append((y - 1, x))
            graph[y - 1][x] = graph[y][x] + 1

        # bottom
        if is_valid_index_y(y + 1, n) and graph[y + 1][x] == 1:
            queue.append((y + 1, x))
            graph[y + 1][x] = graph[y][x] + 1

    print(graph[n-1][m-1])
