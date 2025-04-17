a, b = map(int, input().split())
MAX = (10 ** 16).bit_length()
acc = [0] * MAX
acc[0] = 1
for i in range(MAX):
    acc[i] = (1 << i) + 2 * acc[i - 1]
def calc(n):
    ans = 1 & n
    for i in range(MAX, 0, -1):
        if n & (1 << i):
            ans += acc[i - 1] + n - (1 << i) + 1
            n -= 1 << i
    return ans
print(calc(b) - calc(a - 1))