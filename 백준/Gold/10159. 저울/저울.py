import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

# 인접 행렬 초기화
adj_matrix = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj_matrix[a - 1][b - 1] = 1

# 연결된 노드 체크
# 거치는 노드
for k in range(n):
    # 시작 노드
    for i in range(n):
        # 종료 노드
        for j in range(n):
            if adj_matrix[i][k] and adj_matrix[k][j]:
                adj_matrix[i][j] = 1

for i in range(n):
    result = 0
    for j in range(n):
        if i == j:
            continue
        # i, j가 연결 되어 있지 않으면, 크기 비교를 알 수 없음
        if not adj_matrix[i][j] and not adj_matrix[j][i]:
            result += 1
    print(result)

