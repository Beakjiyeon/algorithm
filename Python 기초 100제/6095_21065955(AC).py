n = int(input())
arr = [[0 for col in range(19)] for row in range(19)]
for i in range(n):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(arr[i][j], end=' ')
    print()
