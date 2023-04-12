def dfs(connect_info, v):
    visited = [False] * (n + 1)
    visited[v] = True
    stack = [v]

    while stack:
        # 스택으로 처음 들어온 노드가 가장 마지막에 나가도록
        node = stack.pop()
        if node == v or not visited[node]:
            print(node, end=' ')
            visited[node] = True
        for x in reversed(connect_info[node]): # 스택이므로 작은 노드부터
            if not visited[x]: # and x not in stack
                stack.append(x)


def bfs(connect_info, n, v):
    from collections import deque
    queue = deque()
    queue.append(v)
    visited = [False] * (n + 1)
    visited[v] = True
    while queue:
        # 큐로 처음 들어온 노드가 제일 먼저 나가도록
        node = queue.popleft()
        print(node, end=' ')
        for x in connect_info[node]:
            if not visited[x]:
                queue.append(x)
                visited[x] = True


def get_connect_info(n, m):
    # input 입력 받기
    graph = []
    for _ in range(m):
        a, b = map(int, input().split())
        graph.append([a, b])

    # 0~n 번 노드에 연결된 노드 목록 정리
    connect_info = [[] for _ in range(n + 1)]
    for g in graph:
        connect_info[g[0]].append(g[1])
        connect_info[g[1]].append(g[0])

    # 방문할 수 있는 정점이 여러 개인 경우 번호 작은 수 정렬
    for x in connect_info:
        x.sort()
    return connect_info


if __name__ == '__main__':
    # 노드 수, 간선 수, 시작 노드 번호
    n, m, v = map(int, input().split())

    # 각 노드가 연결된 정보가 담긴 그래프
    connect_info = get_connect_info(n, m)

    dfs(connect_info, v)
    print()
    bfs(connect_info, n, v)
