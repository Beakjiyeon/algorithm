def subset_sum_count(index, current_sum, cnt):
    if index == len(numbers):
        if current_sum == S and cnt > 0: # cnt : 부분 수열 최소 개수는 1
            return 1
        return 0

    # 현재 원소를 포함하는 경우와 포함하지 않는 경우로 나눠서 재귀 호출
    include = subset_sum_count(index + 1, current_sum + numbers[index], cnt + 1)
    exclude = subset_sum_count(index + 1, current_sum, cnt)

    return include + exclude


# 입력 받기
N, S = map(int, input().split())
numbers = list(map(int, input().split()))

# 결과 출력
result = subset_sum_count(0, 0, 0) 
print(result)
