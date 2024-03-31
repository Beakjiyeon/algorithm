n = int(input())
fees = list(map(int, input().split()))
total_budget = int(input())

start = 1
end = max(fees)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for fee in fees:
        if fee > mid:
            total += mid
        else:
            total += fee

    if total <= total_budget:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)