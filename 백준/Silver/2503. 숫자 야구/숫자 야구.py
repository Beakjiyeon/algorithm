from itertools import permutations


def get_results(guess, results):
    can = []
    # 세자리니까 모든 경우의 수를 다 구한다.
    for p in permutations('123456789', 3):
        strike = sum(p[i] == guess[i] for i in range(3))
        ball = sum(guess[i] in p for i in range(3)) - strike  # 위치가 다른데 숫자가 일치 하는 경우의 수를 구하기 위해 strike 경우 빼줌
        if results == (strike, ball):
            can += [p]
    return can


# 모든 입력 결과에 대해 가능한 조합 리스트를 구하고, 이전 입력 결과에서 가능한 조합과 겹치는 것만 result 리스트에 남김
result = []
for _ in range(int(input())):
    guess, strike, ball = map(int, input().split())
    can = get_results(str(guess), (strike, ball))
    if result == []:
        result = can
    else:
        # 던진 답 들에 대한 s, b를 모두 조합해야 하므로 단계마다 결과를 계속 좁혀 업데이트
        result = [c for c in can if c in result]

print(len(result))
