k = list(map(int, input()))
if len(k) <= 2:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
else:
    d = k[0] - k[1]
    for i in range(1, len(k) - 1):
        if k[i] - k[i + 1] != d:
            print('흥칫뿡!! <(￣ ﹌ ￣)>')
            break
    else:
        print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')