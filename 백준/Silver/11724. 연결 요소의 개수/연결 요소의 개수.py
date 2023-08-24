import sys
# 재귀 제한 거는 용도라고 함..
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

# 노드 n개, 간선 m개
n, m = map(int, input().split())

# 각 노드에 연결된 노드 정보 리스트 틀 (인덱스 0 비움)
graph = [[] for _ in range(n + 1)]
# 노드 방문 기록 (인덱스 0 비움)
visited = [False] * (n + 1)

# 연결된 m 만큼 각 노드에 연결된 노드 정보 채우기
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
#print()
#print(graph)
def dfs(v):
    #print(f'>> dfs({v})')
    # v 노드 방문 처리
    visited[v] = True
    #print(f'{v} 방문 처리함')
    # v 노드와 연결된 노드 탐색
    #print(f'{v} 와 연결된 노드 탐색: {graph[v]}')
    for node in graph[v]:

        if not visited[node]:
            #print(f'{node} 는 방문 전')
            visited[node] = True
            dfs(node)


count = 0
# 1 부터 n까지 순회
for i in range(1, n + 1):
    # 노드 i가 방문 전 이면
    #print('### ', i)
    if not visited[i]:
        #print(f'{i} 방문 전')
        # 지역 개수 카운트 +1
        count += 1
        #print(f'dfs({i})')
        # x와 연결된 노드를 탐색 하는 dfs 호출
        dfs(i)

print(count)
