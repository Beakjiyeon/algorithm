def func(start):
    if len(arr) == m:
        answers.append(arr[:])
        return

    for i in range(start, len(nums)):
        arr.append(nums[i])
        func(i)
        arr.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    answers = []
    arr = []

    func(0)

    answers = sorted(list(set(map(tuple, answers))))  # 중복 제거 및 정렬

    for a in answers:
        print(*a)