class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

s_init = input()
cur = Node(s_init)
for _ in range(int(input())):
    s = input().split()
    op = int(s[0])
    if op == 1:
        new_node = Node(s[1])
        new_node.prev = cur.prev
        new_node.next = cur
        if cur.prev is not None:
            cur.prev.next = new_node
        cur.prev = new_node
    elif op == 2:
        new_node = Node(s[1])
        new_node.next = cur.next
        new_node.prev = cur
        if cur.next is not None:
            cur.next.prev = new_node
        cur.next = new_node
    elif op == 3:
        if cur.prev is not None:
            cur = cur.prev
    else:
        if cur.next is not None:
            cur = cur.next
    print(f"{cur.prev.data if cur.prev else '(Null)'} {cur.data} {cur.next.data if cur.next else '(Null)'}")