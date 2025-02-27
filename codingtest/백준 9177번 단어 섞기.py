import sys
n = int(sys.stdin.readline())

def dfs(ai, bi):
    global ans
    if ans: return
    if ai + bi == len(ab):
        ans = True
        return
    if ai < len(a) and a[ai] == ab[ai + bi]:
        dfs(ai + 1, bi)
    if bi < len(b) and b[bi] == ab[ai + bi]:
        dfs(ai, bi + 1)

for tc in range(1, n + 1):
    a, b, ab = sys.stdin.readline().strip().split()
    if sorted(a + b) != sorted(ab):
        sys.stdout.write(f'Data set {tc}: no' + '\n')
        continue
    ans = False
    dfs(0, 0)
    sys.stdout.write(f"Data set {tc}: {'yes' if ans else 'no'}" + "\n")