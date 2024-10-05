def solution(num):
    n = len(num)
    pos = {'0': [], '1': []}
    for i in range(n):
        pos[num[i]].append(i)
    ans = [''] * n
    for i in range(len(pos['0']) // 2):
        ans[pos['0'][i]] = '0'
    cnt1 = len(pos['1'])
    for i in range(cnt1 // 2, cnt1):
        ans[pos['1'][i]] = '1'

    print(''.join(ans))

solution(list(input().rstrip()))