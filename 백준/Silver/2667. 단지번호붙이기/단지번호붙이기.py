"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

3
7
8
9
"""

# 한점에 모여 있는 뭉치를 파고 들어 찾는 거니까 dfs


if __name__ == '__main__':
    import sys
    from collections import deque

    # 그래프 길이 입력 받기
    n = int(sys.stdin.readline())

    # 그래프 정보 입력 받기
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip())))
        #graph.append(list(map(int, input())))
    #print(graph)
    target_counts = []  # 결과

    # graph[0][0] 부터 그래프 끝까지 이동 하며 1을 찾는다.
    visited = []  # 방문한 좌표 체크용
    for y in range(len(graph)):  # 그래프가 가진 일차원 배열의 갯수
        for x in range(len(graph[y])):  # 일차원 배열의 길이
            # 해당 좌표 값이 1이고 방문한 적이 없으면
            if graph[y][x] == 1 and (y, x) not in visited:
                # 방문 체크 및 큐에 담는다.
                visited.append((y, x))
                queue = deque()
                queue.append((y, x))

                target_count = 0  # 방문 지점과 연결된 값이 1인 좌표의 수 : 뭉치 별로 세니까 0으로 초기화 한다.

                # 큐가 빌 때까지 방문 한다.
                while queue:
                    cy, cx = queue.popleft()
                    # print(f"현재 타겟: {(cy, cx)}")
                    target_count = target_count + 1

                    # 인덱스 에러가 나지 않고 미방문 상태이고 1 값을 가지면 해당 좌표를 큐와 방문 기록에 넣는다.
                    if cx + 1 < len(graph) and (cy, cx + 1) not in visited and graph[cy][cx + 1] == 1:
                        # 오른 쪽으로 이동 가능
                        queue.append((cy, cx + 1))
                        visited.append((cy, cx + 1))
                    if cx - 1 >= 0 and (cy, cx - 1) not in visited and graph[cy][cx - 1] == 1:
                        # 왼 쪽으로 이동 가능
                        queue.append((cy, cx - 1))
                        visited.append((cy, cx - 1))
                    if cy - 1 >= 0 and (cy - 1, cx) not in visited and graph[cy - 1][cx] == 1:
                        # 위 쪽으로 이동 가능
                        queue.append((cy - 1, cx))
                        visited.append((cy - 1, cx))
                    if cy + 1 < len(graph) and (cy + 1, cx) not in visited and graph[cy + 1][cx] == 1:
                        # 아래 쪽으로 이동 가능
                        queue.append((cy + 1, cx))
                        visited.append((cy + 1, cx))

                # 특정 좌표와 연결된 좌표의 수를 저장한다.
                target_counts.append(target_count)

    # 결과를 출력 한다.
    print(len(target_counts))
    target_counts.sort()
    for target_count in target_counts:
        print(target_count)
