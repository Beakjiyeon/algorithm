'''

7
6
1 2
2 3
1 5
5 2
5 6
4 7

4
'''


if __name__ == '__main__':
    m = int(input())
    n = int(input())

    graph = [[] for i in range(1) for j in range(m + 1)]
    
    for _ in range(n):
        a, b = map(int, input().split(' '))
        graph[a].append(b)
        graph[b].append(a)

    from collections import deque
    queue = deque()
    queue.append(1)

    answer = 0
    visited = [1]
    while queue:
        x = queue.popleft()
        for k in graph[x]:
            if k not in visited:
                queue.append(k)
                visited.append(k)
    print(len(visited) - 1)