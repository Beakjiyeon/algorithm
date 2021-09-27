array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 두번째 원소부터 마지막 원소까지 순
    for j in range(i, 0, -1): # i부터 1까지 감소 (현재 원소를 기준으로 왼쪽 원소들과 비교)
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
print('result', array)
