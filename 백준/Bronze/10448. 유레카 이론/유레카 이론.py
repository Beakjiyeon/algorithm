# 삼각수를 동적으로 생성
triangle_number = [n * (n + 1) // 2 for n in range(1, 46)]

# 1,000까지의 수 중 3개의 삼각수의 합으로 나타낼 수 있는 수를 표시
eureka = [0] * 1001
for i in triangle_number:
    for j in triangle_number:
        for k in triangle_number:
            if i + j + k <= 1000:
                eureka[i + j + k] = 1

# 테스트 케이스에 대해 결과 출력
N = int(input())
for _ in range(N):
    x = int(input())
    print(eureka[x])