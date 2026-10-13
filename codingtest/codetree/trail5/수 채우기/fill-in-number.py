n = int(input())
if n < 5 and n % 2 != 0: print(-1)
else:
    ans = 0
    div, mod = divmod(n, 5)
    if mod % 2 and div > 0:
        mod += 5
        div -= 1
    mod = (n - div * 5) // 2
    print(div + mod)