input = open(0).readline

def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    mv = arr[0]
    ans = 0
    for x in arr:
        if x < mv: mv = x
        if x - mv > ans: ans = x - mv
    print(ans)

main()