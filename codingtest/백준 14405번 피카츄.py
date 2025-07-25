a = ['pi', 'ka', 'chu']
s = input()
for x in a: s = s.replace(x, '')
print('YES' if not s else 'NO')