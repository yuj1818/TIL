import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().strip().split())
    all = set(range(n))
    subject = {'kor': set(), 'eng': set(), 'math': set(), '-': all}
    fruit = {'apple': set(), 'pear': set(), 'orange': set(), '-': all}
    color = {'red': set(), 'blue': set(), 'green': set(), '-': all}
    for i in range(n):
        s, f, c = input().strip().split()
        subject[s].add(i)
        fruit[f].add(i)
        color[c].add(i)
    for _ in range(m):
        s, f, c = input().strip().split()
        print(len(subject[s]&fruit[f]&color[c]))

main()