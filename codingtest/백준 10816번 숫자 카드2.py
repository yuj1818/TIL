N = int(input())
counts = {}
cards = list(map(int, input().split()))
for card in cards:
    counts[card] = counts.get(card, 0)
    counts[card] += 1
M = int(input())
needs = list(map(int, input().split()))
for need in needs:
    print(counts.get(need, 0), end=' ')