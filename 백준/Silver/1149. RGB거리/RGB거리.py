# 동적 계획법을 활용하여 집을 칠하는 최소 비용을 계산하는 함수
def min_cost(n, costs):
    # dp[i][j]: i번째 집을 j색으로 칠했을 때의 최소 비용
    dp = [[0] * 3 for _ in range(n)]

    # 초기값 설정: 첫 번째 집의 비용은 그대로 사용
    dp[0] = costs[0]

    # 다이나믹 프로그래밍
    for i in range(1, n):
        # 현재 집을 빨강으로 칠할 때의 최소 비용
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        # 현재 집을 초록으로 칠할 때의 최소 비용
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        # 현재 집을 파랑으로 칠할 때의 최소 비용
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

    # 결과 출력: 모든 집을 칠하는 비용 중 최솟값 반환
    return min(dp[n-1])

# 입력 처리
N = int(input())  # 집의 수
costs = [list(map(int, input().split())) for _ in range(N)]  # 각 집의 빨강, 초록, 파랑으로 칠하는 비용

# 최소 비용 계산 및 출력
result = min_cost(N, costs)
print(result)