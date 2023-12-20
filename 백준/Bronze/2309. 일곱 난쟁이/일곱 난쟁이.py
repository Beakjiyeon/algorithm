from itertools import combinations

def find_seven_men(heights):
    # 아홉 명 중에서 일곱 명의 조합 생성
    for case in combinations(heights, 7):
        # 일곱 명의 키 합이 100인 경우 출력하고 종료
        if sum(case) == 100:
            for man in sorted(case):
                print(man)
            return 0

# 아홉 난쟁이의 키 입력 받기
heights = [int(input()) for _ in range(9)]

# 함수 호출 및 결과 출력
find_seven_men(heights)