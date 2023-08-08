N = int(input())
words = [input() for _ in range(N)]
for word in sorted(set(words), key=lambda x: (len(x), x)):
    print(word)