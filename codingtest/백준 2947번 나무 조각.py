import sys
input = sys.stdin.readline
seq = input().rstrip().split()
while seq != ['1', '2', '3', '4', '5']:
    for i in range(4):
        if seq[i] > seq[i + 1]:
            seq[i], seq[i + 1] = seq[i + 1], seq[i]
            print(' '.join(seq))