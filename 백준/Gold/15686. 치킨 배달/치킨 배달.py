from itertools import combinations
from math import inf

N, M = map(int, input().split())

graph = []
graph.append([0] * (N+1))
for _ in range(N):
    graph.append([0] + list(map(int, input().split())))

homes = []
stores = []
for i in range(N + 1):
    for j in range(N + 1):
        if graph[i][j] == 1:
            homes.append((i, j))
        elif graph[i][j] == 2:
            stores.append((i, j))

spots = []
answer = 1000000
for store in combinations(stores, M):
    sum_distance = 0
    for home in homes:
        dist = inf
        for x, y in store:
            dist = min(dist, abs(home[0] - x) + abs(home[1] - y))
        sum_distance += dist
    answer = min(answer, sum_distance)
print(answer)
