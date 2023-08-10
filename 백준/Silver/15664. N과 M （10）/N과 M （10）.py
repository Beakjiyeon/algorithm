
def func(start):
    if len(arr) == m:
        answers.append(arr[:])
        return

    for i in range(start, len(nums)):
        if not visited[i]:  # 방문 하지 않은 경우만
            visited[i] = True  # 방문 처리
            arr.append(nums[i])
            func(i + 1)
            visited[i] = False
            arr.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    visited = [False] * n  # 방문 여부
    answers = []
    arr = []

    func(0)
    answers = sorted(list(set(map(tuple, answers))))  # 중복 제거 및 정렬

    for answer in answers:
        print(*answer)
