import sys
sys.setrecursionlimit(10000)


def check_index(location, graph):
    y, x = location[0], location[1]
    if y < 0 or x < 0:
        return False
    if y >= len(graph):
        return False
    if x >= len(graph[0]):
        return False
    return True


def dfs(graph, i, j):
    graph[i][j] = -1
    # 상
    up = (i + 1, j)
    if check_index(up, graph):
        if graph[up[0]][up[1]] == 1:
            dfs(graph, up[0], up[1])
    # 하
    down = (i - 1, j)
    if check_index(down, graph):
        if graph[down[0]][down[1]] == 1:
            dfs(graph, down[0], down[1])

    # 좌
    left = (i, j - 1)
    if check_index(left, graph):
        if graph[left[0]][left[1]] == 1:
            dfs(graph, left[0], left[1])
    # 우
    right = (i, j + 1)
    if check_index(right, graph):
        if graph[right[0]][right[1]] == 1:
            dfs(graph, right[0], right[1])


def get_node_count(graph):
    cnt = 0
    # 그래프 순회
    for i in range(len(graph)):  # 세로 길이
        for j in range(len(graph[i])):  # 가로 길이
            # print(graph[i][j], end=' ')
            if graph[i][j] == 1:
                # 상 하 좌 우 탐색
                dfs(graph, i, j)
                cnt = cnt + 1
    return cnt


def run_case():
    w, h, total = map(int, input().split())  # 밭 가로, 세로, 총 배추 개수
    graph = [[0] * w for _ in range(h)]  # 밭 2차원 배열로 선언

    for _ in range(total):  # 배추 위치 값 설정
        x, y = map(int, input().split())
        graph[y][x] = 1
    # print(graph)
    print(get_node_count(graph)) # 배추가 모여 있는 구역 개수 세기


if __name__ == '__main__':
    case_count = int(input())
    for _ in range(case_count):
        run_case()
