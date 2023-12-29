import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
nums = [x for x in map(int, input().split())]
dic = dict()

for num in enumerate(sorted(list(set(nums)))):
    dic[num[1]] = num[0]

for num in nums:
    print(dic[num], end=" ")