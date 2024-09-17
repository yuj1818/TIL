nums = [0] * 10036
def d(x):
    n = x
    while x:
        n += x % 10
        x //= 10
    return n

for i in range(1, 10001):
    nums[d(i)] = 1
    if not nums[i]:
        print(i)