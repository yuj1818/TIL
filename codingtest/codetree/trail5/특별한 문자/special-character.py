d = dict()
r = set()
for i,x in enumerate(input()):
    if x in r: continue
    if x in d:
        d.pop(x)
        r.add(x)
    else: d[x] = i
if d:
    print(sorted(d.items(), key=lambda x:x[1])[0][0])
else: print('None')

