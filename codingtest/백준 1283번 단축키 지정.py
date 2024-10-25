import sys
input = sys.stdin.readline

def trans(words, i, j):
    words = list(map(list, words))
    words[i][j] = '[' + words[i][j] + ']'
    print(' '.join(''.join(word) for word in words))

def find(keys, words):
    for i in range(len(words)):
        if not keys.get(words[i][0].upper()):
            keys[words[i][0].upper()] = (i, 0)
            trans(words, i, 0)
            return
    else:
        for i in range(len(words)):
            for j in range(1, len(words[i])):
                if not keys.get(words[i][j].upper()):
                    keys[words[i][j].upper()] = (i, j)
                    trans(words, i, j)
                    return
    print(' '.join(words))

keys = dict()

for _ in range(int(input())):
    find(keys, input().split())