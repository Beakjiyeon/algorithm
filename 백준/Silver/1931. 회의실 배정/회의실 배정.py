def greedy(meeting):
    cnt = 0
    start_t = -1
    for time in meeting:
        if time[0] >= start_t:
            start_t = time[1]
            cnt += 1
    return cnt

mCount = int(input())
meeting = []
for i in range(mCount):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting = sorted(meeting, key=lambda time: (time[1], time[0]))
print(greedy(meeting))