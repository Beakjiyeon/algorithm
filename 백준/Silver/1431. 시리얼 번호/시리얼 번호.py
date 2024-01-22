n = int(input())
arrs = []
for _ in range(n):
    arrs.append(input())


def sum_str(v):
    sum = 0
    for a in v:
        if a.isdigit():
            sum += int(a)
    return sum


arrs.sort(key=lambda x: (len(x), sum_str(x), x))
for arr in arrs:
    print(arr)
