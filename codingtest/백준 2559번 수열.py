import sys
input = sys.stdin.readline

def solution(n, k, temps):
    acc_sum = sum(temps[:k])
    mx_temp = acc_sum
    for i in range(k, n):
        acc_sum += temps[i] - temps[i - k]
        if mx_temp < acc_sum: mx_temp = acc_sum
    print(mx_temp)

n, k = map(int, input().split())
temps = list(map(int, input().split()))
solution(n, k, temps)