def solution(s, skip, index):
    ans = ''
    skip = set(skip)
    for i in range(len(s)):
        x = ord(s[i])
        cnt = 0
        while cnt < index:
            x += 1
            if x > 122:
                x = 97
            if chr(x) in skip:
                continue
            cnt += 1
        ans += chr(x)
    return ans
