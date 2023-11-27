def min_moves_to_destination(l, start, destination):
    # 나이트의 이동 가능한 위치
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    # 시작 위치와 목표 위치
    start_x, start_y = start
    dest_x, dest_y = destination

    # BFS를 사용하여 최소 이동 횟수 계산
    queue = [(start_x, start_y, 0)]  # 시작 위치와 현재까지의 이동 횟수를 저장하는 큐
    visited = set()  # 방문한 위치를 기록하는 집합

    while queue:
        current_x, current_y, moves_count = queue.pop(0)

        if current_x == dest_x and current_y == dest_y:
            return moves_count

        for move in moves:
            new_x, new_y = current_x + move[0], current_y + move[1]
            if 0 <= new_x < l and 0 <= new_y < l and (new_x, new_y) not in visited:
                queue.append((new_x, new_y, moves_count + 1))
                visited.add((new_x, new_y))

    return -1  # 목표 위치로 이동할 수 없는 경우

# 테스트 케이스 개수 입력
test_cases = int(input())

for _ in range(test_cases):
    # 체스판의 한 변의 길이와 시작 위치, 목표 위치 입력
    l = int(input())
    start = tuple(map(int, input().split()))
    destination = tuple(map(int, input().split()))

    # 최소 이동 횟수 출력
    result = min_moves_to_destination(l, start, destination)
    print(result)
