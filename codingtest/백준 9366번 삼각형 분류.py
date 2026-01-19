import sys
input = sys.stdin.readline
for tc in range(int(input())):
    arr = sorted(map(int, input().split()))
    ans = 'scalene'
    if arr[0] + arr[1] <= arr[2]: ans = 'invalid!'
    elif arr[0] == arr[1] == arr[2]: ans = 'equilateral'
    elif arr[0] == arr[1] or arr[1] == arr[2] or arr[2] == arr[0]: ans = 'isosceles'
    print(f"Case #{tc + 1}: {ans}")