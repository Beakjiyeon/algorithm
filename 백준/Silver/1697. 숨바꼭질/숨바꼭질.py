from collections import deque

def find_min_time(N, K):
    visited = [False] * 100001  # 방문 여부를 저장하는 배열
    queue = deque([(N, 0)])  # 초기 위치와 시간을 큐에 추가

    while queue:
        current_pos, time = queue.popleft()

        if current_pos == K:
            return time

        # 순간이동: 2*X로 이동
        next_pos = current_pos * 2
        if 0 <= next_pos <= 100000 and not visited[next_pos]:
            queue.append((next_pos, time + 1))
            visited[next_pos] = True

        # 걷기: X-1 또는 X+1로 이동
        for next_pos in (current_pos - 1, current_pos + 1):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                queue.append((next_pos, time + 1))
                visited[next_pos] = True

    return -1  # 동생을 찾을 수 없는 경우

# 입력 받기
N, K = map(int, input().split())

# 결과 출력
result = find_min_time(N, K)
print(result)
