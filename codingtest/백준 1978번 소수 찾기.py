N = int(input())
nums = list(map(int, input().split()))
answer = 0
for i in nums:
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        answer += 1
print(answer)