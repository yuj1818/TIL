import sys

def main():
    input = sys.stdin.read().splitlines()
    left = list(input[0])
    right = []
    for com in input[2:]:
        if com[0] == 'L':
            if left:
                right.append(left.pop())
        elif com[0] == 'D':
            if right:
                left.append(right.pop())
        elif com[0] == 'B':
            if left:
                left.pop()
        elif com[0] == 'P':
            left.append(com[2])
    print(''.join(left + right[::-1]))

if __name__ == "__main__":
    main()