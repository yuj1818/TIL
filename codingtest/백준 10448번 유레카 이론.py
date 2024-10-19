import sys
input = sys.stdin.readline

def main():
    tc = int(input())
    TN = [i * (i + 1) // 2 for i in range(1, 45)]
    TA = [0] * 2971

    for i in range(44):
        for j in range(i, 44):
            for k in range(j, 44):
                TA[TN[i] + TN[j] + TN[k]] = 1

    for _ in range(tc):
        print(TA[int(input())])

if __name__ == '__main__':
    main()