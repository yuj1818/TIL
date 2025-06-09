num = input()
ans = [0] * 10
for n in list(map(int, num)):
    if n == 6 or n == 9:
        if ans[6] <= ans[9]: ans[6] += 1
        else: ans[9] += 1
    else: ans[n] += 1
print(max(ans))