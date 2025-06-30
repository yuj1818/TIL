N, F = [int(input()) for _ in range(2)]
ans = N // 100 * 100
while ans % F != 0: ans += 1
print(str(ans)[-2:])