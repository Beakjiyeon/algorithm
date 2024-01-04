def count_repaints(board):
    repaint_count = float('inf')  # 현재까지의 최소 다시 칠해야 하는 정사각형 개수를 무한대로 초기화

    # 보드에서 가능한 모든 8x8 크기의 체스판을 시도
    for i in range(len(board) - 7):
        for j in range(len(board[0]) - 7):
            # 현재 시작 위치에서의 다시 칠해야 하는 정사각형 개수를 계산
            repaint_count = min(repaint_count, calculate_repaints(board, i, j))

    return repaint_count


def calculate_repaints(board, start_row, start_col):
    repaint_count1 = 0  # 흰색으로 시작하는 경우
    repaint_count2 = 0  # 검은색으로 시작하는 경우

    # 8x8 체스판을 돌면서 각 칸에 대해 다시 칠해야 하는지 확인
    for i in range(8):
        for j in range(8):

            # 현재 좌표가 짝수일 때
            if (i + j) % 2 == 0:
                # 흰색으로 시작한 경우에 짝수자리가 검정이면 다시 칠해야 함
                if board[start_row + i][start_col + j] != 'W':
                    repaint_count1 += 1
                    # 검정으로 시작한 경우에 짝수자리가 하양이면 다시 칠해야 함
                if board[start_row + i][start_col + j] != 'B':
                    repaint_count2 += 1
            # 현재 좌표가 홀수일 때
            else:
                # 흰색으로 시작한 경우에 홀수 자리가 하양이면 다시 칠해야 함
                if board[start_row + i][start_col + j] != 'B':
                    repaint_count1 += 1
                # 검은색으로 시작한 경우에 홀수 자리가 검정이면 다시 칠해야 함
                if board[start_row + i][start_col + j] != 'W':
                    repaint_count2 += 1

    # 두 경우 중에서 최소 다시 칠해야 하는 정사각형 개수 반환
    return min(repaint_count1, repaint_count2)

n, m = map(int, input().split())
board = [input() for _ in range(n)]
print(count_repaints(board))