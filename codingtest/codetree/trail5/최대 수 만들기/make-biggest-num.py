n = int(input())
arr = [input() for _ in range(n)]
arr.sort(key=lambda x: x * 3, reverse=True)
print(''.join(arr))
