N = int(input())
'''
graph = []
for i in range(N):
    row = list(input()) # 문자열을 리스트에 문자 하나씩
    graph.append(row)
'''
graph = [list(input()) for _ in range(N)]

'''
주어진 리스트에서 연속으로 나타나는 최대 문자의 개수를 반환
cnt : 현재 검사 중인 문자의 연속 개수
max_cnt : 현재까지 확인한 최대 연속 문자 개수
리스트를 처음부터 끝까지 반복하면서, 현재 문자와 이전문자가 같으면 cnt를 증가시킴
'''
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
    max_row = max(count_candy_line(row) for row in graph)
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

def swap_and_calculate(swap_function, i, j):
    swap_function(graph, i, j)
    result = count_candy()
    swap_function(graph, i, j)
    return result

result = 1
for i in range(N - 1):
    for j in range(N):
        if graph[i][j] != graph[i + 1][j]:
            result = max(result, swap_and_calculate(swap_down, i, j))


for i in range(N):
    for j in range(N - 1):
        if graph[i][j] != graph[i][j + 1]:
            result = max(result, swap_and_calculate(swap_right, i, j))

print(result)
