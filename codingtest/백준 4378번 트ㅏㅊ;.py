import sys
newK = dict()
normal = ["=-0987654321`", "\][POIUYTREWQ", "';LKJHGFDSA", "/.,MNBVCXZ"]
for r in normal:
    for i in range(1, len(r)):
        newK[r[i - 1]] = r[i]
newK[' '] = ' '
for t in sys.stdin.readlines(): print(''.join(newK[x] for x in t.rstrip()))
