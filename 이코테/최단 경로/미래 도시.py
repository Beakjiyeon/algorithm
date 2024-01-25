n, m = map(int, input().split())

INF = int(1e9)
# a -> b, b -> a  연결 여부를 알 수 있게 그래프 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 연결 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    # 양방향으로 이동 가능
    graph[a][b] = 1
    graph[b][a] = 1

# 소개팅 노드 x, 최종 목적지 k
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][k] + graph[k][x]
if result >= INF:
    print(-1)
else:
    print(result)

'''
입력
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

출력
3


입력
4 2
1 3
2 4
3 4

출력
-1
'''
