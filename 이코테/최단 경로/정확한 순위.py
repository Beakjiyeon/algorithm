n, m = map(int, input().split())

# 학생 a, b 성적 비교 가능 여부
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 비교 가능할 때 = 연결되어 있다고 봄 = 1 할당
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 연결 가능성이 있는지 플로이드 워셜 이용
# 거치는 노드
for k in range(1, n + 1):
    # 시작 노드
    for a in range(1, n + 1):
        # 종료 노드
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

# 순위를 정확히 알 수 있는 학생 수
result = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        # 다른 노드와 서로 도달이 가능한지 체크
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    # 순위를 알 수 있다.
    if count == n:
        result += 1
print(result)

'''
입력
6 6
1 5
3 4
4 2
4 6
5 2
5 4

출력
1
'''
