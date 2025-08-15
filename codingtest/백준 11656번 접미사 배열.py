s = open(0).readline().strip()
ans = [s[-1]]
for i in range(len(s) - 2, -1, -1): ans.append(s[i] + ans[-1])
ans.sort()
print('\n'.join(ans))