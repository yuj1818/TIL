N = int(input())
num_list = list(map(int, input().split()))
increase = 1
decrease = 1
answer = 0
for i in range(1, N):

    if num_list[i] > num_list[i - 1]:
        if decrease > 1:
            answer = max(answer, decrease)
            decrease = 1
        increase += 1
    elif num_list[i] < num_list[i - 1]:
        if increase > 1:
            answer = max(answer, increase)
            increase = 1
        decrease += 1
    else:
        increase += 1
        decrease += 1
answer = max(answer, increase, decrease)
print(answer)