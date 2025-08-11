s = ''
while 1:
    try:
        s += input().strip()
    except:
        break
print(sum(map(int, s.split(','))))