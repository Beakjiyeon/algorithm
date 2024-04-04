n = int(input())
a = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

a.sort()


def is_num_exist(num):
    # 이진 탐색
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if num == a[mid]:
            return True
        elif num > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return False


for num in arr:
    if is_num_exist(num):
        print(1)
    else:
        print(0)
