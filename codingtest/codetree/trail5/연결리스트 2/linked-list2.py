class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

def pop(x):
    if x.prev is not None:
        x.prev.next = x.next
    if x.next is not None:
        x.next.prev = x.prev
    x.prev = None
    x.next = None

def appendLeft(x, y):
    y.prev = x.prev
    y.next = x
    if y.prev is not None:
        y.prev.next = y
    if y.next is not None:
        y.next.prev = y

def append(x, y):
    y.prev = x
    y.next = x.next
    if y.prev is not None:
        y.prev.next = y
    if y.next is not None:
        y.next.prev = y

n = int(input())
nd = {i + 1: Node(i + 1) for i in range(n)}

for _ in range(int(input())):
    op, *nums = input().split()
    if op == '1':
        i = int(nums[0])
        pop(nd[i])
    elif op == '2':
        i, j = map(int, nums)
        appendLeft(nd[i], nd[j])
    elif op == '3':
        i, j = map(int, nums)
        append(nd[i], nd[j])
    elif op == '4':
        i = int(nums[0])
        print(nd[i].prev.data if nd[i].prev else 0, nd[i].next.data if nd[i].next else 0)

for i in range(1, n + 1):
    print(nd[i].next.data if nd[i].next else 0, end=' ')
