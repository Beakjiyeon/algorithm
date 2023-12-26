n = int(input())
prices = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        # print(f'dp[{i}] = max(dp[{i}], dp[{i - j}] + prices[{j}])')
        dp[i] = max(dp[i], dp[i - j] + prices[j])

print(dp[n])