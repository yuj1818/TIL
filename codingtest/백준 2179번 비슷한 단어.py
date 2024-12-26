import sys
input = sys.stdin.readline

def main():
    n = int(input())
    words = [input().rstrip() for i in range(n)]
    pred = {}
    for word in words:
        tmp = ''
        for x in word:
            tmp += x
            pred[tmp] = pred.get(tmp, 0) + 1
    mpre = ''
    m = 0
    for pre, cnt in pred.items():
        if cnt > 1 and len(pre) > m:
            mpre = pre
            m = len(pre)
    cnt = 0
    for word in words:
        if mpre == word[:m]:
            cnt += 1
            print(word)
        if cnt == 2: break

main()