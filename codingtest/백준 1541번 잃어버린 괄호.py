f = input()
nums = []
n = ''
for i in range(len(f)):
    if f[i].isdigit():
        n += f[i]
    else:
        nums.append(int(n))
        n = ''
        nums.append(f[i])
nums.append(int(n))
stack = []
sum_v = []
sign = 1
for num in nums:
    if num == '-':
        sum_v.append(sum(stack) * sign)
        stack = []
        sign = -1
    elif type(num) == int:
        stack.append(num)
sum_v.append(sum(stack) * sign)
print(sum(sum_v))