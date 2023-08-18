def func():
    if len(arr) == m:
        answers.append(arr[:])
        return

    for i in range(len(nums)):
        arr.append(nums[i])
        func()
        arr.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    answers = []
    arr = []

    func()
    answers = sorted(list(set(map(tuple, answers))))  # 중복 제거 및 정렬

    for answer in answers:
        print(*answer)