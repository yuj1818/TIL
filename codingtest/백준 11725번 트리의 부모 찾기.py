import sys
input = sys.stdin.readline

def main():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    ans = [0]*(n+1)
    ans[1] = -1
    s = graph[1]
    for i in graph[1]: ans[i] = 1
    while s:
        for w in graph[(node:=s.pop())]:
            if not ans[w]:
                s.append(w)
                ans[w] = node
    print(*ans[2:], sep='\n')

main()