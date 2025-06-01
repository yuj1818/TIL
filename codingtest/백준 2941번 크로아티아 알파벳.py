ca = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input().strip()
ans = 0
for a in ca:
    ans += s.count(a)
    s = s.replace(a, ' ')
print(ans + len(s.replace(' ', '')))