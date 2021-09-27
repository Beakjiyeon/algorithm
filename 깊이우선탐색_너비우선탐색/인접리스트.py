# 행이 3개인 2차원 리스트로 인접 리스트 표현
graph [[] for _ in range(3)]

# 노드0에 연결된 노드 정보 저장
graph[0].append((1, 7)) # (노드1, 노드0과 노드1의 간선 비용)
graph[0].append((2, 5)) # (노드2, 노드0과 노드2의 간선 비용)

# 노드1에 연결된 노드 정보 저장
graph[1].append((0, 7))

# 노드2에 연결된 노드 정보 저장
graph[2].append((0, 5))

print(graph)