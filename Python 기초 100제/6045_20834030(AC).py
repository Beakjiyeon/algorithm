﻿'''
정수 3개가 공백을 두고 입력된다.

출력
합과 평균을 공백을 두고 출력한다.
평균은 소숫점 이하 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.
'''
a, b, c = map(int, input().split())
sum = a + b + c
avg = sum / 3 
print(sum, format(avg, ".2f"))
