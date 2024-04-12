# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

#import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


def count_block(matrix):
    global min_cnt
    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j]:
                cnt += 1
    min_cnt = min(min_cnt, cnt)


def delete_block(board, x, y, weight):
    # 해당 블록 터뜨리기
    board[x][y] = 0
    # 해당 블록이 영향 미치는 블록까지 터뜨리기
    if weight > 1:
        for i in range(1, weight):
            for dx, dy in delta:
                nx, ny = x + dx * i, y + dy * i
                if 0 <= nx < h and 0 <= ny < w:
                    # 영향 미쳐진 블록이 영향을 주는 블록까지 터뜨리기
                    delete_block(board, nx, ny, board[nx][ny])



# 중력 적용
def down_block(board):
    new_board = [[0] * w for _ in range(h)]
    # 각 열에 대해
    for wi in range(w):
        # 행 수 줄이기 : 질문 왜  + 가 아니지
        init = h - 1
        for hi in range(init, -1, -1):
            # 블록 값이 있다면
            if board[hi][wi]:
                # 새 보드에는 한 행 줄여서 넣기.. 연쇄 실행
                new_board[init][wi] = board[hi][wi]
                init -= 1
    return new_board

def game_start(matrix, n):
    # 구슬 모두 소진
    if n == 0:
        count_block(matrix)
        return

    # 열 개수 만큼 순회하면서 보드 복사
    for drop in range(w):
        board = [row[:] for row in matrix]
        # 행, 열 (행은 맨 위 부터 시작)
        x, y = 0, drop
        # drop 열에서 가장 윗 행에 있는 블록 찾기
        while x < h and not board[x][y]:
            x += 1
        # 만약 해당 열에 블록이 없으면, 다음 열로 이동
        if x == h:
            count_block(board)
            continue
        # drop 열에서 가장 윗 행에 있는 블록을 기준으로 터뜨리기
        delete_block(board, x, y, board[x][y])
        #
        board = down_block(board)
        game_start(board, n - 1)


for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    n, w, h = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(h)]
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    min_cnt = float('inf')
    game_start(matrix, n)
    print(f'#{test_case} {min_cnt}')


    # ///////////////////////////////////////////////////////////////////////////////////
