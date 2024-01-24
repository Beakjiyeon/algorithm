n, m = map(int, input().split())

# 1. 간선 정보 목록
edges = []

# 2. 부모 정보 초기화
parent = [i for i in range(0, n + 1)]

# 3. 간선 정보 초기화
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 4. 간선 비용 순으로 정렬
edges.sort()  # 리스트의 원소가 튜플일 경우 기본적으로 튜플의 첫 번째 요소를 기준으로 정렬


def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union_parent(a, b):
    # 최종 부모와 합치기
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 5. 간선 확인하기
result = 0
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에 집합에 포함한다.
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost
        last = cost  # 가장 큰 간선을 뺴서 마을 2개로 분리한다.

print(result - last
      )
'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
