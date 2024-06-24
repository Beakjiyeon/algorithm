def dfs(day, profit):
    global max_profit
    if day >= N:
        max_profit = max(max_profit, profit)
        return
    # 상담을 하지 않는 경우
    dfs(day + 1, profit)
    # 상담을 하는 경우
    if day + consultations[day][0] <= N:
        dfs(day + consultations[day][0], profit + consultations[day][1])

N = int(input())
consultations = [tuple(map(int, input().split())) for _ in range(N)]
max_profit = 0
dfs(0, 0)
print(max_profit)
