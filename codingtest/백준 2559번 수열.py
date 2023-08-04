N, K = map(int, input().split())
temp_list = list(map(int, input().split()))
init_sum = sum(temp_list[:K])
max_temp = init_sum
idx = K
for i in range(K, N):
    init_sum = init_sum - temp_list[i - K] + temp_list[i]
    if max_temp < init_sum:
        max_temp = init_sum
    idx += 1
print(max_temp)