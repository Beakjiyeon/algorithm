k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]
# 이진 탐색을 위해 정렬
cables.sort()

start = 1
end = max(cables)

result = -1
while start <= end:
    # mid 길이씩 잘랐을 때
    mid = (start + end) // 2

    cnt = 0
    for cable in cables:
        if cable >= mid:
            cnt += cable // mid

    # 케이블이 n 이상이면 되므로 cnt >= n, cnt < n 으로 나눠준다.
    if cnt >= n:
        start = mid + 1
        if result < mid:
            result = mid
    else:  # 잘랐을 때 개수가 적게 나오면, 늘려야 하므로 너비를 줄여야 함
        end = mid - 1
    # else:  # 잘랐을 때 개수가 많이 나오면, 줄여야 하므로 너비를 늘려야 함
    #     start = mid + 1

print(result)

'''
# 추가 반례
입력)
4 4
9
9
9
10
출력)
9

# 반례 출처
https://velog.io/@taehyeon96/%EB%B0%B1%EC%A4%801654-%EB%9E%9C%EC%84%A0-%EC%9E%90%EB%A5%B4%EA%B8%B0%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89
'''