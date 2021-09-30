# 재귀 방식
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)
def fibo(x):
    print('f(' + str(x) + ')', end=' ') # 호출되는 함수
    if  x == 1 or x == 2: # 종료 조건
        return 1
    if d[x] != 0: # 이미 계산한 적 있는 문제라면 그대로 반환
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

# 출력 결과 :
'''
f(99) f(98) f(97) f(96) f(95) f(94) f(93) f(92) f(91) f(90) f(89) f(88) f(87) f(86) f(85) f(84) f(83) f(82) f(81) f(80) f(79) f(78) f(77) f(76) f(75) f(74) f(73) f(72) f(71) f(70) f(69) f(68) f(67) f(66) f(65) f(64) f(63) f(62) f(61) f(60) f(59) f(58) f(57) f(56) f(55) f(54) f(53) f(52) f(51) f(50) f(49) f(48) f(47) f(46) f(45) f(44) f(43) f(42) f(41) f(40) f(39) f(38) f(37) f(36) f(35) f(34) f(33) f(32) f(31) f(30) f(29) f(28) f(27) f(26) f(25) f(24) f(23) f(22) f(21) f(20) f(19) f(18) f(17) f(16) f(15) f(14) f(13) f(12) f(11) f(10) f(9) f(8) f(7) f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4) f(5) f(6) f(7) f(8) f(9) f(10) f(11) f(12) f(13) f(14) f(15) f(16) f(17) f(18) f(19) f(20) f(21) f(22) f(23) f(24) f(25) f(26) f(27) f(28) f(29) f(30) f(31) f(32) f(33) f(34) f(35) f(36) f(37) f(38) f(39) f(40) f(41) f(42) f(43) f(44) f(45) f(46) f(47) f(48) f(49) f(50) f(51) f(52) f(53) f(54) f(55) f(56) f(57) f(58) f(59) f(60) f(61) f(62) f(63) f(64) f(65) f(66) f(67) f(68) f(69) f(70) f(71) f(72) f(73) f(74) f(75) f(76) f(77) f(78) f(79) f(80) f(81) f(82) f(83) f(84) f(85) f(86) f(87) f(88) f(89) f(90) f(91) f(92) f(93) f(94) f(95) f(96) f(97) 218922995834555169026
'''
