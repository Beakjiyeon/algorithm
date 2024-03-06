n = int(input())

row = 1
max_count = 0
while True:
    max_count += row

    if n <= max_count:
        # print(f'{row}번째 ')
        break
    row += 1

# 이전 줄 까지의 분수 개수
cnt_by_prev_row = max_count - row

# n 번 째 분수는 row 줄의 몇 번 째
th_in_current_row = n - cnt_by_prev_row

if row % 2 == 0:
    result = f'{th_in_current_row}/{int(row) - int(th_in_current_row) + 1}'
else:
    result = f'{int(row) - int(th_in_current_row) + 1}/{th_in_current_row}'
print(result)