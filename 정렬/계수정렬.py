# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언 및 0으로 초기화
# ex. 최댓값이 9일 경우, 0 ~ 9 므로 9 +1 = 10
count = [0] * (max(array) + 1) 

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트의 첫 번째 데이터부터
    for j in range(count[i]): # 등장횟수만큼 인덱스 출력
        print(i, end=' ')

# 출력 결과 : 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9