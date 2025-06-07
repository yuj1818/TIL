input = open(0).readline
for _ in range(int(input())):
    a, b = input().strip().split()
    print(f"{a} & {b} are {'NOT ' if sorted(a) != sorted(b) else ''}anagrams.")