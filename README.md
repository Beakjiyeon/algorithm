## 🌈 algorithm
* 알고리즘 문제를 푸는 저장소입니다.
 
### 입력 팁
* 정수형 2개 입력 받기
~~~
a,b = map(int, input().split())
~~~
* 정수형 n개 입력 받기
~~~
arr = list(map(int,input().split()))
~~~
* 정수형 2개 입력 받기 (좀 더 빠르게 입력받기)
~~~
import sys
n, m = map(int, sys.stdin.readline().split())
~~~
* 2차원 리스트 입력 받기
~~~
board = [list(map(int, sys.stdin.readline().split())) for _in range(n)]
~~~
* 문자열 입력 받기
~~~
text = sys.stdin.readline().rstrip()
~~~

### 배열 팁
* 1차원 배열 초기화
~~~
rows = 10
arr = [0] * rows
~~~
* 2차원 배열 초기화
~~~
rows = 10
cols = 5
arr = [[0 for j in range(cols)] for i in range(rows)]
~~~


### 참고 레퍼런스
* https://velog.io/@sjy5386/Python-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%EC%84%A0%EC%96%B8%ED%95%98%EA%B8%B0
* https://paris-in-the-rain.tistory.com/72
