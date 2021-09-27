from collections import deque

# BFS
def bfs(graph, start, visited):
	# 큐 구현을 위해 deque 라이브러리 사용
	queue = deque([start])
	# 현재 노드를 방문 처리
	visited[start] = True

	# 큐가 빌때까지 반복
	while queue:
		v = queue.popleft()
		print(v, end=' ')
		# 해당 원소와 인접한, 아직 방문하지 않은 원소들을 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

# 인접 리스트 : 각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [
			[], # 0번 노드와 인접한 노드
    		[2, 3, 8],
    		[1, 7],
    		[1, 4, 5],
    		[3, 5],
    		[3, 4],
    		[7],
    		[2, 6, 8],
    		[1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)

# 출력결과 : 1 2 3 8 7 4 5 6