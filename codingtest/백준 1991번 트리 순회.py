class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, child, isLeft):
        if isLeft:
            self.left = child
            return
        else:
            self.right = child
            return

    def preorder(self):
        if self != None:
            print(chr(self.value + 65), end='')
            if self.left: self.left.preorder()
            if self.right: self.right.preorder()

    def inorder(self):
        if self != None:
            if self.left: self.left.inorder()
            print(chr(self.value + 65), end='')
            if self.right: self.right.inorder()

    def postorder(self):
        if self != None:
            if self.left: self.left.postorder()
            if self.right: self.right.postorder()
            print(chr(self.value + 65), end='')

import sys
input = sys.stdin.readline
n = int(input())
arr = [TreeNode(i) for i in range(n)]
for _ in range(n):
    p, l, r = map(lambda x: ord(x) - 65 if ord(x) > 64 else None, input().rstrip().split())
    if l: arr[p].insert(arr[l], True)
    if r: arr[p].insert(arr[r], False)
arr[0].preorder()
print()
arr[0].inorder()
print()
arr[0].postorder()