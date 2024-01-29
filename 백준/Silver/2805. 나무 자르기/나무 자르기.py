n, m = map(int, input().split())  # 나무의 수, 베어야 하는 나무
trees = list(map(int, input().split()))
trees.sort()  # 나무의 길이를 정렬
# 절단기 범위 : 최소 길이는 1, 최대 길이는 가장 긴 나무의 길이로 설정
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2

    total_length = 0
    for tree in trees:
        if tree > mid:
            # 잘리는 나무 길이
            total_length += tree - mid

    # mid 와 타겟(잘리는 나무의 합) 비교
    # 잘리는 길이가 m보다 크면, 덜 절단 해도 됌 (절단기 수치 올리기)
    if total_length >= m:
        start = mid + 1
    # 잘리는 길이가 부족하면, 더 절단해야 함(절단기 수치 내리기)
    else:
        end = mid - 1

print(end)
