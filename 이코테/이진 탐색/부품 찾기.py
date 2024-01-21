n = int(input())
store = list(map(int, input().split()))

m = int(input())
order = list(map(int, input().split()))


def binary_search(array, target, start, end):
    array.sort()
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


# 이진 탐색
def binary_method():
    for o in order:
        idx = binary_search(store, o, 0, n - 1)
        if idx is None:
            print("no", end=" ")
        else:
            print("yes", end=" ")


# 집합
def set_method():
    for o in order:
        if o in store:
            print("yes", end=" ")
        else:
            print("no", end=" ")


# 계수 정렬
def idx_method():
    array = [0] * 1000001
    for s in store:
        array[s] = 1

    for o in order:
        if array[o] == 1:
            print("yes", end=" ")
        else:
            print("no", end=" ")


idx_method()

'''
5 
8 3 7 9 2
3
5 7 9
'''
