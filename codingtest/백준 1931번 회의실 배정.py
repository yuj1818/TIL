from sys import stdin
input = stdin.readline
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))
reservation = [meetings[0]]
for i in range(1, N):
    if meetings[i][0] >= reservation[-1][1]:
        reservation.append(meetings[i])
print(len(reservation))