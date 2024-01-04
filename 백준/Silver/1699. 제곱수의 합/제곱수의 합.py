
import sys
input=sys.stdin.readline

n=int(input())

dp=[0]*100001

for i in range(1, n+1):
	#제곱수로 이루어진 숫자일때
    if int(i**0.5)==i**0.5:
        dp[i]=1
    else:
        min_value=1e9
        # 1부터 i의 제곱근까지만 해야 dp[-1]와 같은 out of index를 피한다.
        for j in range(1, int(i**0.5)+1):
            min_value=min(min_value, dp[i-j**2])
        dp[i]=min_value+1

print(dp[n])