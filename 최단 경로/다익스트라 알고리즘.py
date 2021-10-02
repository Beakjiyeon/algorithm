import heapq # 우선순위 큐
import sys
input = sys.stdin.readline 
INF = int(1e9)

n, m = map(int, input().split()) # 노드 개수, 간선 개수
start = int(input()) # 시작 노드 번호

# 그래프 생성
graph = [[] for _ in range(n + 1)]

# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n + 1) 

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # a번 노드에서 b번 노드로 가는 비용이 c. (노드, 거리)

def dijkstra(start):
    q = []
    # 시작 노드 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 힙에서 최단거리 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 이미 방문했던 노드라면
        if distance[now] < dist: 
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1] # 비용
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리
for i in range(1, n +1):
    if distance[i] ==INF :
        print("INFINITY")
    else:
        print(distance[i])
        
'''
# 입력
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

# 출력 
0
2
3
1
2
4
'''

