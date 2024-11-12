import sys
input = sys.stdin.readline

def main():
    h, w = map(int, input().split())
    blocks = list(map(int, input().split()))
    midx = blocks.index(max(blocks))
    ans, mv = 0, 0
    for i in range(midx + 1):
        if mv < blocks[i]: mv = blocks[i]
        ans += mv
    mv = 0
    for i in range(w - 1, midx, -1):
        if mv < blocks[i]: mv = blocks[i]
        ans += mv
    print(ans - sum(blocks))
    
main()