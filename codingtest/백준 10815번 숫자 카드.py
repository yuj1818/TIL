import sys

def main():
    cards, comps = sys.stdin.read().split('\n')[1::2]
    cards = set(cards.split())
    comps = comps.split()
    print(' '.join("1" if n in cards else "0" for n in comps))

if __name__ == '__main__':
    main()