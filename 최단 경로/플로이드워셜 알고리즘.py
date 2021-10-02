INF = int(1e9)

# 노드 개수, 간선 개수
n = int(input())
m = int(input())

# 2차원 리스트 생성 및 초기화 (배열인덱스 = 노드번호 로 하기 위해 n + 1)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b :
            graph[a][b] = 0

# 각 간선 정보 입력
for _ in range(m):
    # A에서 B로 가는 비용 C
    a, b, c = map(int, input().split())
    graph[a][b] = c


# 점화식에 따라 플로이드워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()


'''
# 입력
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

# 출력
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0

'''
