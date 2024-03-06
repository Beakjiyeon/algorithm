n, k = map(int, input().split())
coins = []
for v in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

result = 0
for coin in coins:
    if k // coin != 0:  # 몫
        result += k // coin
        k = k % coin  # 나머지
print(result)