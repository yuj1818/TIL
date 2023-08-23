L = int(input())
s = input()
code = dict()
for i in range(97, 123):
    code[chr(i)] = i - 96
H = sum([code[s[i]] * (31 ** i) for i in range(L)]) % 1234567891
print(H)