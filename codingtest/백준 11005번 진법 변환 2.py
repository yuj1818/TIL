n, b = map(int, input().split())
ans = ''
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while n:
    ans += number[n % b]
    n //= b
print(ans[::-1])