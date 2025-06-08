def trans(n, x): return int(n.replace('5' if x else '6', '6' if x else '5'))
a, b = input().split()
print(trans(a,0)+trans(b,0), trans(a,1)+trans(b,1))