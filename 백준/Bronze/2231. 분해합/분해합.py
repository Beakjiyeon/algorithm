N = int(input())

for m in range(1, N + 1):
    n = m + sum(list(map(int,str(m))))
    if n == N:
        print(m)
        exit()
print(0)
        