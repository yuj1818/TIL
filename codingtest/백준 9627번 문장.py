def calc(x):
    one = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
           'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    ten = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if x < 20:
        return one[x]
    if x < 100:
        return ten[x // 10] + one[x % 10]
    return one[x // 100] + 'hundred' + calc(x % 100)

n = int(input())
s = [input().strip() for _ in range(n)]
l = sum(map(len, s)) - 1
for i in range(1, 1000):
    res = calc(l + i)
    if len(res) + l == l + i:
        s[s.index('$')] = res
        break
print(*s)