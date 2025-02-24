def main():
    s = open(0).readline().strip()
    s = s.replace('<', '!<').replace('>', '>!')
    words = s.split('!')
    words = [v for v in words if v]
    ans = ''
    for word in words:
        if word[0] == '<':
            ans += word
        else:
            arr = word.split(' ')
            for i, x in enumerate(arr):
                ans += x[::-1]
                if i < len(arr) - 1: ans += ' '
    print(ans)

main()