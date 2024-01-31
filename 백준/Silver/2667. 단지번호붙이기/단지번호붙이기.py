from collections import deque

n = int(input())

# 그래프 정보 입력 받기
graph = []
visited = []
for _ in range(n):
    graph.append(list(map(int, input())))
    #visited.append(list([False] * n))
    visited.append([False] * n)
# visited[0][0] = True

#print(visited)
def bfs(graph, visited, n):
    dx = [-1, 1, 0, 0]  # 상, 하
    dy = [0, 0, -1, 1]  # 좌, 우

    queue = deque()
    result = []

    for a in range(0, n):
        for b in range(0, n):
            #print('###', x, y)
            if graph[a][b] == 1 and visited[a][b] == False:
                visited[a][b] = True
                queue.append((a, b))
                v_count = 0

                while queue:
                    x, y = queue.popleft()
                    v_count += 1
                    #print('#####', x, y)
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0 <= nx < n and 0 <= ny < n:
                            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                                # print('###=', nx, ny)
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                # v_count += 1
                #print(x, y, v_count)
                result.append(v_count)

    return result


result = bfs(graph, visited, n)

print(len(result))
result.sort()
for target_count in result:
    print(target_count)


'''
5
11110
00000
11100
00000
11000
3
2
3
3
'''