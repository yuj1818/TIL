def main():
    import sys
    input = sys.stdin.readline
    pairs = [input().split() for _ in range(int(input()))]
    pairs.sort(key= lambda x: x[1], reverse=True)
    pairs.sort(key= lambda x: x[0])
    print('\n'.join(f'{o} {i}' for o, i in pairs))

if __name__ == '__main__':
    main()