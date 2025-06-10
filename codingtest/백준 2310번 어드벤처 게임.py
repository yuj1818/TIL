from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def main():
    while 1:
        n = int(input())
        if n == 0: break
        rooms = [[]]
        for i in range(n):
            w, f, *arr, _ = input().split()
            arr = list(map(int, arr))
            rooms.append([(int(f) if w == 'T' else -int(f)), arr])
        if rooms[1][0] > 0:
            print('No')
            continue
        pq = []
        visited = [0] * (n + 1)
        heappush(pq, (0, 1))
        while pq:
            c, r = heappop(pq)
            if visited[r]: continue
            visited[r] = 1
            for x in rooms[r][1]:
                if visited[x]: continue
                f = rooms[x][0]
                if f > 0:
                    if c + f > 0: continue
                    heappush(pq, (c + f, x))
                else: heappush(pq, (min(c, f), x))
        print('Yes' if visited[n] else 'No')

if __name__ == '__main__': main()