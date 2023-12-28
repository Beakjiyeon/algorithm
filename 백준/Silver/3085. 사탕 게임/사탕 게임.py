
N = int(input())

graph = []
for i in range(N):
    row = list(input())
    graph.append(row)

def count_candy_line(line):
    cnt = 1
    max_cnt = 1
    for i in range(1, N):
        if line[i] == line[i - 1]:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt
def count_candy():
    
    # 가로
    max_row = max(count_candy_line(row) for row in graph)

    # 세로
    max_col = max(count_candy_line([graph[i][m] for i in range(N)]) for m in range(N))


    return max(max_row, max_col)


def swap_down(graph, i, j):
    tmp = graph[i][j]
    graph[i][j] = graph[i + 1][j]
    graph[i + 1][j] = tmp

def swap_right(graph, i, j):
    tmp = graph[i][j]
    graph[i][j] = graph[i][j + 1]
    graph[i][j + 1] = tmp


result = 1
for i in range(N - 1):
    for j in range(N):
        if graph[i][j] != graph[i + 1][j]:
            swap_down(graph, i, j)
            d = count_candy()
            swap_down(graph, i, j)
            result = max(result, d)


for i in range(N): # j만 값 변화 있으니까 범위 n 설정
    for j in range(N - 1):
        if graph[i][j] != graph[i][j + 1]:
            swap_right(graph, i, j)
            r = count_candy()
            swap_right(graph, i, j)
            result = max(result, r)
print(result)