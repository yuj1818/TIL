import sys
input = lambda x: [-int(x[1]), int(x[2]), -int(x[3]), x[0]]

def main():
    scores = [input(sys.stdin.readline().split()) for _ in range(int(sys.stdin.readline()))]
    sys.stdout.write('\n'.join(list(map(lambda x: x[3], sorted(scores)))))

main()